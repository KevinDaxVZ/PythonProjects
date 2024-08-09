#!/usr/bin/python3
"""
CREAR EL JUEGO DEL MICHI INTERACTIVO
ESTE JUEGO ESTA DISEÑADO PARA 2 JUGADORES
Autor: Kevin Dax Victorio Zanabria"""

import os
import random
import platform


def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def dibujar_juego():
    for i in range(4):
        for j in range(4):
            print(game_inicio[i][j], end=' ')
        print('')

def jugada(jugador):
    while True:
        try:
            dibujar_juego()
            print("Turno de {}".format(jugador))
            print("{} es {}".format(jugador, jugadores[jugador]))
            x, y = input('Indique sus coordenadas a marcar: ').split(' ')
            x = int(x)
            y = int(y)

            if x in [1,2,3] and y in [1,2,3]:
                if (x,y) not in ocupado:
                    ocupado.append((x,y))
                    game_inicio[x][y] = jugadores[jugador]
                    break
                else:
                    print('Esa posicion ya esta ocupada, intentelo de nuevo...')
            else:
                print("No ingresaste una posicion valida, valores permitridiso [1-3]")

        except:
            print("----ERROR----")
            print("Debes ingresar 2 numeros enteros entres entre [1-3] separados por un espacio")

        input(".......Presione Cualquier tecla para continuar......")
        limpiar_pantalla()


def celebrar(jugador):
    print('!!!FELICIDADES {} GANASTE!!!'.format(jugador))
    dibujar_juego()
    return False

def empate():
    for i in range(1,4):
        if '_' in game_inicio[i]:
            return True

    print('NADIE HA GANADO, ES UN EMPATE')
    dibujar_juego()
    return False

def comprobar_ganador(jugador):

    #COMPROBANDO POR FILAS Y COLUMNAS:
    for i in range(1,4):
        if game_inicio[i][1] == game_inicio[i][2] and game_inicio[i][2] == game_inicio[i][3] and game_inicio[i][1] != '_':
            return celebrar(jugador)

        elif game_inicio[1][i] == game_inicio[2][i] and game_inicio[2][i] == game_inicio[3][i] and game_inicio[1][i] != '_':
            return celebrar(jugador)

    #COMPROBANDO POR DIAGONALES
    if game_inicio[1][1] == game_inicio[2][2] and game_inicio[2][2] == game_inicio[3][3] and game_inicio[2][2] != '_':
        return celebrar(jugador)

    elif game_inicio[3][1] == game_inicio[2][2] and game_inicio[2][2] == game_inicio[1][3] and game_inicio[2][2] != '_':
        return celebrar(jugador)

    else:
        return empate()


if __name__=='__main__':
    #SE DEFINEN LOS JUGARES Y SUS NOMBRES
    player1 = input("Ingrese el nombre del jugador 1: ")
    player2 = input("Ingrese el nombre del jugador 2: ")

    #SE DEFINEN SUS FICHAS
    jugadores = {player1: 'x', player2: 'O'}

    #SE CONSTRUYE LA MATRIZ
    game_inicio = [['_' for i in range(4)] for j in range(4)]
    for i in range(4):
        game_inicio[0][i] = str(i)
        game_inicio[i][0] = str(i)
    game_inicio[0][0] = '/'

    ocupado=[]

    #SE ELIJE AL PRIMER JUGADOR
    jugador = random.choice([player1, player2])

    #A JUGAR
    #RONDAS
    bandera = True
    while bandera:
        limpiar_pantalla()
        jugada(jugador)
        bandera = comprobar_ganador(jugador)
        if jugador == player1:
            jugador = player2
        else:
            jugador = player1

    print('')
    print('')
    print('')
    input('')
