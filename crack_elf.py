#!/usr/bin/python3

import sys
import subprocess
import colorama
from concurrent.futures import ThreadPoolExecutor

def main():
    """f_leer = ['super_secret_password'] <-- POSSIBLE PASSWORD"""
    archivo = sys.argv[2]

    if sys.argv[1].lower() == '-h' or sys.argv[1] == '--hh':
        help()
        exit()

    with open(archivo,'r',encoding='latin-1') as f:
        f_leer = [linea.strip() for linea in f.readlines()]


    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(attack,f_leer)


def attack(password):
    
        result = subprocess.run([sys.argv[1],password],capture_output=True,text=True)

        message = sys.argv[3]

        if message not in result.stdout:
            print(result.stdout.strip(),end=' ')
            print(f'{colorama.Fore.GREEN}\tPASSWORD: {password}{colorama.Fore.RESET}')
            
            with open('correct_password.txt','a') as f:
                 f.write(password)

            exit()

        else:
            print(f'{colorama.Fore.RED}{result.stdout.strip()}',end=' ')
            print(f'\tfor PASSWORD: {password}{colorama.Fore.RESET}')
            

def help():
    print('Correct example use: ')
    print('\tcracking_ELF.py NAMEPROGRAM WORDLIST MESSAGE\n')
    print('\tcracking_ELF.py ./cracking4 /usr/share/wordlist/rockyou.txt "Acces Denied"')


if __name__ == "__main__":
    if len(sys.argv) == 4:
            main()

    else:
         help()
