# ENGAÑA AL GOBIERNO CON ESTE SCRIPT
# ESTE SCRIPT PERMITE ENVIAR VOTOS BOTOS A UN PROYECTO PARA HACERLO GANAR
# Autor: KDvz

def main():
    os.system('cls')
    # credenciales = input('Ingresa el nombre de tu txt: ')
    credenciales = 'credenciales.txt'
    # num_bots = int(input("Por favor, introduce el número de bots: "))
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


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from concurrent.futures import ThreadPoolExecutor
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver
from colorama import Fore
# from selenium.webdriver.edge.service import Service
import os
from seleniumbase import Driver
import random
import re

def navega():
    # driver = Driver(headless=False)
    # driver.set_window_size(400, 915)

    # ----------------------------------MODIFICANDO EL USER AGENT DEL CHROME----------------------------------------

    user_agents = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12"
    ]



    desired_user_agent = random.choice(user_agents)
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={desired_user_agent}")

    print(desired_user_agent)

    # -----------------------anti-cloudflare
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('--disable-extensions')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-browser-side-navigation')
    options.add_argument('--disable-gpu')
    # options.add_argument('--auto-open-devtools-for-tabs')

    # options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    driver.get('https://wb2server.congreso.gob.pe/spley-portal/#/expediente/2021/8291')
    driver.switch_to.window(driver.window_handles[0])
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                '.p-button-raised.p-button-rounded.p-button-danger.p-button.p-component')))



    # PARA CERRAR EL INSPECCIONAR
    # driver.execute_script("window.dispatchEvent(new KeyboardEvent('keydown', {'key': 'F12'}));")

    # ABRIMOS LA 2DA VENTANA Y PROCEDEMOS A EXTRAER EL CORREO ELECTRINCO
    driver.execute_script("window.open('https://tempail.com/es/');")
    driver.switch_to.window(driver.window_handles[1])

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'eposta_adres')))

    mi_correo = email_input.get_attribute('value')  # aqui obtuvimos el correo random

    time.sleep(2)

    # AQUI VOLVEMOS A LA VENTANA PARA RELLENAR LOS DATOS
    driver.switch_to.window(driver.window_handles[0])

    driver.switch_to.window(driver.window_handles[0])
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                '.p-button-raised.p-button-rounded.p-button-danger.p-button.p-component'))).click()

    return driver, mi_correo


def elemento_presente(driver):
    driver.switch_to.window(driver.window_handles[1])



    while True:
        driver.refresh()
        try:
            WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.avatar'))).click()
            break
        except:
            pass


    while True:
        try:
            driver.refresh()
            # Esperar a que el iframe esté presente y cambiar el contexto al iframe usando su id
            iframe_id = 'iframe'
            iframe_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, iframe_id)))
            driver.switch_to.frame(iframe_element)

            # Esperar a que el elemento <strong> esté presente dentro del iframe
            strong_element_xpath = '//p[contains(text(),"Mediante la presente, se le envía el código de validación para el registro:")]/strong'
            strong_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, strong_element_xpath)))

            # Obtener el texto del elemento <strong>
            texto_completo = strong_element.text
            clave = re.search(r'\d+', texto_completo).group()

            # Cambiar el contexto de vuelta al contenido principal
            driver.switch_to.default_content()
            break
        except:
            pass


    driver.switch_to.window(driver.window_handles[0])

    parent_div = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.wrapper.ng-star-inserted'))
    )

    xpath_x = parent_div.get_attribute('id')
    xpath_y = xpath_x.split('_')[1]
    i = 0

    #PARA PONER EL CODIGO
    for e in clave:
        while True:
            try:
                xpath = f'otp_{i}_{xpath_y}'
                WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.ID, xpath))).send_keys(e)
                break
            except:
                pass

        i = i + 1

    time.sleep(2)

    #ENVIAR COIDGO
    xpath = '//*[@id="p-fieldset-0-content"]/div/cr-btn-registrar-opinion/cr-modal-registrar-opinion/p-dialog/div/div/div[3]/button[1]'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))).click()

    return driver


def check_login(driver, correo):
    try:
        # sellecionar TRATAMIENTO
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.ng-tns-c52-6.p-dropdown.p-component'))).click()

        # Definimos si es señor o señorita

        xpath = '//*[@id="p-fieldset-2-content"]/div/div[2]/div[1]/p-dropdown/div/div[3]/div/ul/p-dropdownitem[1]/li/span'
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))).click()

        # seleccionar SEXO
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.ng-tns-c52-7.p-dropdown-label.p-inputtext.p-placeholder.ng-star-inserted'))).click()

        xpath = '//*[@id="p-fieldset-2-content"]/div/div[2]/div[2]/p-dropdown/div/div[3]/div/ul/p-dropdownitem[1]/li/span'
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))).click()

        # PARA DAR CLIC EN 'USAR EL DEPARTAMENTE DEL DNI
        xpath = '//*[@id="p-fieldset-3-content"]/div/div/div[1]/p-checkbox/div/div[2]'
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))).click()

        # PARA INDICAR LA POSICION A FAVOR

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.ng-tns-c52-9.p-dropdown-label.p-inputtext.p-placeholder.ng-star-inserted'))).click()

        xpath = '//*[@id="p-fieldset-3-content"]/div/div/div[3]/p-dropdown/div/div[3]/div/ul/p-dropdownitem[1]/li/span'
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))).click()

        # PARA RELLENAR EL CUADRO DE COMENTARIOS
        xpath = '//*[@id="opinion"]'
        comment_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)))

        comment_box.send_keys('POR UN FUTURO MEJOR')


        # PARA PONER UN CORREO ELECTRONICO
        xpath = '//*[@id="p-fieldset-4-content"]/div/div/div[1]/input'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))).send_keys(correo)


        # PARA ENVIAR EL CODIGO
        xpath = '//*[@id="p-fieldset-4-content"]/div/div/div[2]/button'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))).click()

        #PARA COMPROBAR QUE SE ENVIO EL CODIGO
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.wrapper.ng-star-inserted')))

    except:
        print('-------------ALGO FALLO-------------------')

    time.sleep(2)


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


def scrolleando(driver):

    time.sleep(5)
    xpath = '//*[@id="p-fieldset-0-content"]/div/cr-btn-registrar-opinion/cr-modal-registrar-opinion/p-dialog/div/div/div[2]/form/div'
    # Esperar hasta que el div con la clase 'ng-tns-c84-1 p-dialog-content' sea visible
    scrollable_div = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, xpath)))

    scrollable_div.click()
    time.sleep(1)
    # Utilizar JavaScript para desplazar hasta la parte inferior del elemento
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)


    # Esperar a que el botón se haga clickeable después de hacer scroll
    xpath = '//*[@id="p-fieldset-0-content"]/div/cr-btn-registrar-opinion/cr-modal-registrar-opinion/p-dialog/div/div/div[3]/button[1]'
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, xpath))).click()


    #Enviando la opinion final
    xpath = '/html/body/div[3]/div/div[3]/button[2]'
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, xpath))).click()





def enviar_login(driver, usuario, password):

    driver.switch_to.default_content()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'dni')))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'dni'))).send_keys(usuario)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'digitoControl'))).send_keys(password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                '.p-button-danger.w-100.p-button.p-component.ng-star-inserted'))).click()



    # Esperar a que el elemento que contiene el texto sea visible
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="p-fieldset-2-content"]/div/span')))


def procces_login(driver, usuario, password, correo):
    try:
        enviar_login(driver, usuario, password)
        check_login(driver, correo)
        clave = elemento_presente(driver)
        scrolleando(driver)
        return clave

    except:
        return False

def handle(logins):
    usuario, password = logins
    driver, correo = navega()
    try:
        clave = procces_login(driver, usuario, password, correo)

        if clave:
            print('Se envio el formulario correctamente para')
            print(f'DNI: {usuario} CODIGO_VERIFICACION: {password} <---> CORREO: {correo}   -  clave: {clave}\n')

        else:
            print('No se envio para')
            print(f'DNI: {usuario} CODIGO_VERIFICACION: {password} <---> CORREO: {correo}   -  clave: {clave}\n')
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
