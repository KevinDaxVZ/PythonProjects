# aqui voy a desarrollar el juego del michi
import random
import os

# construire el tablero
def mostar_tabla(tabla):
    for i in range(4):
        if i == 0:
            print('  1 2 3')
            continue
        for j in range(4):
            if j == 0:
                print(f'{i}',end=' ')
                continue
            print(tabla[i-1][j-1],end=" ")
        print("")

def crear_tablero():
    tabla = []
    for i in range(3):
        fila = []
        for j in range(3):
            fila.append('-')
        tabla.append(fila)
    return tabla

def comprobar_empate(tabla):
    for fila in tabla:
        if '-' in fila:
            return False
    return True


def comprobar_ganador(tabla):
    for i in range(3):
        if tabla[0][i] == tabla[1][i] == tabla[2][i] and tabla[2][i]!='-':
            return True
        if tabla[i][0] == tabla[i][1] == tabla[i][2] and tabla[i][2]!='-':
            return True

    if tabla[0][0] == tabla[1][1] == tabla[2][2] and tabla[i][i] != '-':
        return True
    if tabla[0][2] == tabla[1][1] == tabla[2][0] and tabla[i][2-i]!='-':
        return True

    return False

marcas = {input("Ingrese el nombre del jugador#1: "):'X',input("Ingrese el nombre del jugador#2: "):'O'}
tabla = crear_tablero()
i = random.choice([0,1])
os.system('cls')
print("\033[34mComenzando el juego....\033[0m") 
mostar_tabla(tabla)
while True:
    if i%2 == 0:
        jugador = list(marcas.keys())[0]
    else:
        jugador = list(marcas.keys())[1]

    print(f"{jugador.capitalize()}: Elije tu movimiento [{marcas[jugador]}]")

    while True:
        print("fila:                ")
        print("Columna:             ")
        fila, columna = input("\033[2Ffila:"), input("Columna: ")
        if fila  in ['1','2','3'] and columna  in ['1','2','3']:
            if tabla[int(fila)-1][int(columna)-1] == '-':
                break
            else:
                print('\033[3F\033[33m[Mal movimiento]\033[0m posición ya ocupada')
        else: 
            print('\033[3F\033[31m[Mal movimiento]\033[0m Valores permitidos solo entre [1-3]')

    tabla[int(fila)-1][int(columna)-1] = marcas[jugador]

    os.system("cls")
    mostar_tabla(tabla)

    if comprobar_ganador(tabla):
        print(f"GANA EL JUGADOR {jugador.capitalize()}:{marcas[jugador]}")
        break
    if comprobar_empate(tabla):
        print("NADIE GANA, EMPATE")
        break
    i+=1
