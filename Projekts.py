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