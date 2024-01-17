from os import system
from turtle import clear
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import PySimpleGUI as sg
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
import time
# strftime(%d) iespejams vajag ar "%d"

# Payload ievade
usr = input("Lūdzu ievadīt lietotājvārdu: ")
pwd = input("Lūdzu ievadīt paroli: ")
system('clear')

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

# Sākuma lapas atvēršana
url = "https://estudijas.rtu.lv/"
driver.get(url)
time.sleep(2)

# Pieslēgšanās
find = driver.find_element(By.ID, "submit")
find.click()
find = driver.find_element(By.ID, "IDToken1")
find.send_keys(usr)
find = driver.find_element(By.ID, "IDToken2")
find.send_keys(pwd)
find = driver.find_element(By.NAME, "Login.Submit")
find.click()

# Izvilkšana
find = find = driver.find_element(By.CLASS_NAME, "day-number")
day = find.get_attribute("value")
print(day)
input()

#paraug dati
event_list = []
event = ["Projekts", "19.01.24", "Lietotājprogrammas"]
event_list.append(event)
event = ["piemers", "20.01.24", "Lietotājprogrammas"]
event_list.append(event)

def log_in(): #iegust log in informāciju lai nolasītu no svarīgā konta
    sg.theme('LightBlue')
    payload = []
    layout = [  [sg.Text('Ievadat ortusa informāciju')],
                [sg.Text('Lietotājvārds'), sg.InputText()],
                [sg.Text('Parole'), sg.Push(),sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    window = sg.Window('Log in', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            exit()
        if event == 'Ok':
            payload = [values[0],values[1]] #log in dati
            return payload

def period():# iegūst e-pastu uz kuru sūtīt info un laika periodu no kura nolasīt info
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

def display_info(page):#attēlo iegūtos datus ar opciju nosūtīt atgādinājumu 
    sg.theme('LightBlue')
    layout = [ [sg.Text(f'Tuvākais termiņš ir:'), sg.Push(),sg.Text(event_list[page][0], font=("bold"))],
               [sg.Text(f'To vajag iesniegt līdz:'), sg.Push(),sg.Text(event_list[page][1], font=("bold"))],
               [sg.Text(f'Kurss kurā to vajag izdarīt:'), sg.Push(),sg.Text(event_list[page][2], font=("bold"))],
               [sg.Button('Atgādināt'), sg.Button('Tālāk')] ]
    
    window = sg.Window('Darbi', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            exit()
        if event == 'Atgādināt':
            #send_email() #fun
            break
        if event == 'Tālāk':
            try:
                display_info((page+1)) #rekursijas princips datu izskatīšanai
                break
            except IndexError:
                break

log_in()
period()
display_info(page)