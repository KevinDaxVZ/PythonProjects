#JUEGO DE PIEDRA, PAPEL Y TIJERA
#Autor: Kevin Dax Victorio Zanabria
#INSTALE COLORAMA PARA MAS DINAMISMO    # en su terminal escriba 'pip install colorama'

import platform
import random
import os
from colorama import Fore


def definir_ganador(yo,pc):

    if pc == 0:
        if yo == 0:
            return f"{Fore.YELLOW}:/ empato :/"
        elif yo == 1:
            return f"{Fore.RED}:( Usted perdio :( "
        else:
            return f"{Fore.GREEN}!!!Usted gano :D ¡¡¡"

    elif pc == 1:
        if yo == 0:
            return f"{Fore.GREEN}!!!Usted gano :D ¡¡¡"
        elif yo == 1:
            return f"{Fore.YELLOW}:/ Usted empato :/"
        else:
            return f"{Fore.RED}:( Usted perdio :( "

    else:
        if yo == 0:
            return f"{Fore.RED}:( Usted perdio :( "
        elif yo == 1:
            return f"{Fore.GREEN}!!! :D Usted gano :D ¡¡¡"
        else:
            return f"{Fore.YELLOW}:/ Usted empato :/"

def limpiar_pantalla():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def empezar_juego():
    opciones = {0: 'papel', 1: 'piedra', 2: 'tijera'}

    computadora = random.choice(list(opciones.keys()))

    print("=========*** OPCIONES VALIDAD [ 1 2 3 ] ***=========")
    print('1.papel')
    print('2.piedra')
    print('3.tijera')

    try:
        opc = int(input('Elije tu mano: ')) - 1

        if opc in opciones.keys():
            print('\n')
            print('La computadora elijio: ----> {}'.format(opciones[computadora]))
            print('         Usted elijio: ----> {}'.format(opciones[opc]))

            print("Usted ", definir_ganador(opc, computadora))


        else:
            print('No elijio una mano validad...')

    except:
        print('No ingreso un numero....')


def background_color():

    while True:
        lista_i = [i for i in range(10)] + ['a','b','c','d','e','f']
        i = random.choice(lista_i)
        j = random.choice(lista_i)

        if i == j:
            continue
        else:
            break


    color_bg = f'color {i}{j}'
    os.system(color_bg)


if __name__ == "__main__":
    bandera = True

    while bandera:


        empezar_juego()

        print('')
        print('')
        print('¿Jugar de nuevo?... [Presione \'S\' para jugar de nuevo]')
        again = input('')

        limpiar_pantalla()

        if again.lower() == 's':
            background_color() if platform.system() == 'Windows' else ''
            continue

        else:
            bandera = False
