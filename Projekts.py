from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import PySimpleGUI as sg
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import datetime

def scrape(usr,pwd): # Izvilkšana
    service = Service()
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=option)
    url = "https://estudijas.rtu.lv/"
    driver.get(url)
    time.sleep(2)

    find = driver.find_element(By.ID, "submit")
    find.click()
    find = driver.find_element(By.ID, "IDToken1")
    find.send_keys(usr)
    find = driver.find_element(By.ID, "IDToken2")
    find.send_keys(pwd)
    find = driver.find_element(By.NAME, "Login.Submit")
    find.click()
    find = driver.find_element(By.LINK_TEXT, "Atvērt kalendāru...")
    find.click()
    find = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/section/div/div/div[1]/div/div[2]/div").text
    data = find.split('\n')

    # Datu sakārtošana
    pos = 0
    nextpos = 0
    event_list=[]
    for i in range(len(data)):
        if "Kursa notikums" in data[i] and pos == 0:
            pos = i
        elif "Kursa notikums" in data[i] and pos != 0:
            nextpos = i    
        elif pos and nextpos !=0:
            event_list.append(data[pos-2:nextpos-2])
            pos = nextpos
            nextpos = 0
        elif i==len(data)-1:
            nextpos = i
            event_list.append(data[pos-2:nextpos])
        else : continue
    return event_list

def log_in(): #iegust log in informāciju lai nolasītu no svarīgā konta
    sg.theme('LightBlue')
    payload = []
    layout = [  [sg.Text('Ievadat ortusa informāciju')],
                [sg.Text('Lietotājvārds'), sg.InputText()],
                [sg.Text('Parole'), sg.Push(), sg.InputText(password_char='*')],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    window = sg.Window('Log in', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            exit()
        if event == 'Ok':
            payload = [values[0],values[1]] #log in dati
            return payload

def period():# iegūst e-pastu uz kuru sūtīt info #laika periodu no kura nolasīt info
    sg.theme('LightBlue')
    layout = [  [sg.Text('Ievadat e-pastu un laika periodu')],
                [sg.Text('e-pasts'), sg.InputText()],
                [sg.CalendarButton('Līdz kuram datumam', target='-CAL1-', pad=None, key='-CAL1-', format=('%Y-%m-%d'))],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    window = sg.Window('period', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            exit()
        if event == 'Ok':
            return values

page = 0 #darbu skaitītājs

def display_info(page, event_list):#attēlo iegūtos datus ar opciju nosūtīt atgādinājumu 
    sg.theme('LightBlue')
    layout = [ [sg.Text(f'Tuvākais darbs ir:'), sg.Push(),sg.Text(event_list[page][0], font=("bold"))],
               [sg.Text(f'To vajag iesniegt līdz:'), sg.Push(),sg.Text(event_list[page][1], font=("bold"))],
               [sg.Text(f'Kurss kurā to vajag izdarīt:'), sg.Push(),sg.Text(event_list[page][3], font=("bold"))],
               [sg.Button('Atgādināt'), sg.Button('Tālāk')] ]
    
    window = sg.Window('Darbi', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            exit()
        if event == 'Atgādināt':
            try:
                send_email(event_list[page]) #fun
                display_info((page+1), event_list)
                break
            except IndexError:
                break
        if event == 'Tālāk':
            try:
                display_info((page+1), event_list) #rekursijas princips datu izskatīšanai
                break
            except IndexError:
                exit()

def send_email(event_list):
    sender_email = '' #šeit ievieto epastu no kura tiks sūtīti atgādinājumi
    sender_password = '' #konta/aplikācijas parole
    receiver_email = notif_email
    subject = f'Atādinājums par darbu {event_list[2]}' #add name
    body = f'Jums ir jaiesniedz {event_list[0]} līdz {event_list[1]}' #add name and time

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
    except Exception as e:
        return

    month_mapping = {
    'janvāris': 1,
    'februāris': 2,
    'marts': 3,
    'aprīlis': 4,
    'maijs': 5,
    'jūnijs': 6,
    'jūlijs': 7,
    'augusts': 8,
    'septembris': 9,
    'oktobris': 10,
    'novembris': 11,
    'decembris': 12
    }

    parts = event_list[1].split(', ')

    day = int(parts[1].split('.')[0]) #iegūst dienas skaitli
    month_name = parts[1].split(', ')[1].split(', ')[0].lower()
    month = month_mapping.get(month_name)  #iegūst mēneša skaitli

    date_info = event_list[1].split(',')
    print(date_info)
    scheduled_date = datetime(2024, month, day, 12, 0, 0)
    schedule.every().at("12:00").do(send_email,scheduled_date)
    return display_info(page+1,event_list)

exe = False

# Keep the script running to allow the scheduler to work
while True:
    schedule.run_pending()
    time.sleep(1)

    if not exe:
        usr, pwd = log_in()
        notif_email = period()
        event_list = scrape(usr, pwd)
        display_info(page, event_list)

        exe = True