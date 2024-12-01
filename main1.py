import random
import time
import msvcrt
import os

def call_Tablero(n):
    return [['-' for i in range(n)] for i in range(n)]

def generar_manzana(n):
    pos_manzana = [random.randint(0,n-1),random.randint(0,n-1)]
    return pos_manzana

def snake(y,x):
    return y,x

if __name__ == "__main__":
    n = 10
    tabl = call_Tablero(n)
    pos_snake = snake(int(n/2 +1),int(n/2))
    tabl[pos_snake[0]][pos_snake[1]] = 'C'
    vely = -1
    velx = 0
    bandera = True
    cuerpo = []
    ii = 0
    bandera2 = True

    ban = True
    while ban:
        key = ''
        os.system('cls')
        tabl = call_Tablero(n)

        if msvcrt.kbhit():  # Verifica si se presionó una tecla
            key = msvcrt.getch()  # Lee la tecla

            if key == b'q' or key == b'Q':
                print('\tSaliendo del juego...')
                exit()   

            elif key == b'\xe0':  # Las teclas especiales (como flechas) comienzan con este byte
                key = msvcrt.getch()  # Lee el siguiente byte para identificar la tecla

        if key == b'K':  # Flecha izquierda
            velx = -1
            vely = 0
        elif key == b'H':  # Flecha arriba
            vely = -1
            velx = 0
        elif key == b'P':  # Flecha abajo
            vely = 1
            velx = 0
        elif key == b'M':  # Flecha derecha
            velx = 1
            vely = 0

        cuerpo.append([pos_snake[0], pos_snake[1]])
        bandera2 = True
        for i,j in cuerpo[-1+ii:][::-1]:
            if bandera2:
                tabl[i][j] = '☻'
                bandera2 = False
            else:
                tabl[i][j] = '◙'

        pos_snake = pos_snake[0] + vely , pos_snake[1] + velx

        if pos_snake[0] >= n or pos_snake[0] <0 or pos_snake[1] >= n or pos_snake[1]<0:
            print('\t\t*** !PERDISTE DAS LASTIMA MI AMOR¡ ***')
            exit()

        while bandera:
            pos_manzana = generar_manzana(n)
            if tabl[pos_manzana[0]][pos_manzana[1]] == '-':
                bandera = False

        tabl[pos_manzana[0]][pos_manzana[1]] = 'M'
        
        if tabl[pos_snake[0]][pos_snake[1]] == 'M':
            bandera = True
            bandera2 = True
            ii -= 1 



        if tabl[pos_snake[0]][pos_snake[1]] == '◙':
            tabl[pos_snake[0] - vely][pos_snake[1] - velx] = '◙'
            tabl[pos_snake[0]][pos_snake[1]] = 'X'
            print('\t\t*** !PERDISTE DAS LASTIMA MI AMOR¡ ***')
            ban = False

        ganar = True
        for i in tabl:
            for j in i:
                if '-' in j:
                    ganar = False
                print(j,end = ' ')

            print()

        if ganar:
            print('♥♥♥ FELICIDADES, FUISTE EL MEJOR DE TODOS, HAS GANADO ♥♥♥')
            ban = False

        time.sleep(1)
