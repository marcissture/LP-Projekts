from os import system
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import PySimpleGUI as sg
import time
from getpass import getpass
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# strftime(%d) iespejams vajag ar "%d"

# Payload ievade
usr = input("Lūdzu ievadīt lietotājvārdu: ")
pwd = getpass(prompt="Lūdzu ievadīt paroli: ")
system('clear')

# Sākuma lapas atvēršana
service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)
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
find = driver.find_element(By.LINK_TEXT, "Atvērt kalendāru...")
find.click()

# Izvilkšana
data = []
find = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/section/div/div/div[1]/div/div[2]/div").text
data.append(find)
sdata = [s.split('\n') for s in data]

## Datu sakārtošana
# eventpos = []
# event=[]
# all_events=[]
# for i in split_data:
#     if "tiks slēgts" or "ir pieejams" or "atveras" in split_data[i]:
#         eventpos.append(i)
#     if len(eventpos) == 2:
#         for k in range(eventpos[0], eventpos[1]):
#             event.append(split_data[k])
#         all_events.append(event)
#         eventpos = []
# print(event)
# input()


def log_in():
    sg.theme('DarkAmber')   # Add a touch of color
    payload = []
    # All the stuff inside your window.
    layout = [  [sg.Text('Ievadat ortusa informāciju')],
                [sg.Text('Lietotājvārds'), sg.InputText()],
                [sg.Text('Parole'), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Log in', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Ok':
            break

    payload = [values[0],values[1]]
    return payload

def display_info():
    sg.theme('DarkAmber')
    layout = [ [sg.Text('Tuvākais termiņš ir darbam ')],
               [sg.Text('To vajag iesniegt līdz ')],
               [sg.Text('Kurss kurā to vajag izdarīt ')],
               [sg.Text('Saite ')],
               [sg.Button('Atgādināt'), sg.Button('Tālāk')] ]
    
    window = sg.Window('Darbi', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Atgādināt':
            #send_email() #fun
            break
        if event == 'Tālāk':
            display_info() #fun tikai citi mainīgie
            break
    
    return