import pygame
import random
import math
import os
import re
import datetime
import pathlib
import sys
import io
import shutil
import time

#This is the classic game to shoot bullets at aliens that are approaching you to destroy you.



#------------------DEFINIRA LA POSICION DONDE SE MOSTRARA LA PANTALLA CREADA POR PYGAME SOBRE LA PANTALLA DEL SISTEMA----------
if True:
    # Define la posición de la ventana en la pantalla
    x_position = 200
    y_position = 50

    # Establece la posición de la ventana
    os.environ['SDL_VIDEO_WINDOW_POS'] = "{},{}".format(x_position, y_position)


inicio=time.time()
#INICIAMOS LOS OBJETOS DE PYGAME Y CREAMOS LA PANTALLA
if True:
    pygame.init()
    pygame.display.set_caption('Invasion Extraterrestre')
    icon_imagen=pygame.image.load('ovni.png')
    pygame.display.set_icon(icon_imagen)

#PANTALLA
if True:
    pantalla=pygame.display.set_mode((800,600))
    fondo_imagen=pygame.image.load('Fondo.jpg')    #fondo
    pantalla.blit(fondo_imagen,(0,0))

#------SONIDO-------------
#Fondo
if True:
    pygame.mixer.music.load('MusicaFondo.mp3')
    pygame.mixer.music.set_volume(.2)
    pygame.mixer.music.play(-1)                         #dentro de parentesis se indica cuantas veces se va repetir, sino pones nada por defecto es 1 vez, si pones -1 es infinitas veces.


#LOOP MENU INICIO-----------------------------------------
if True:
    enemigos_cantidad=0
    v=0
    bala_movy = 0
    def sonido_clic():
        mus=pygame.mixer.Sound('Golpe.mp3')
        mus.set_volume(0.2)
        mus.play()


    facil_fuente=pygame.font.Font('FreeSansBold.ttf',50)
    facil_texto=facil_fuente.render(' Facil ',True,(255,255,255),(200,200,100))
    f=True
    fn=False
    def facil():
        global v,bala_movy
        bala_movy = -1
        v=0.2
        return 5

    normal_fuente=pygame.font.Font('FreeSansBold.ttf',50)
    normal_texto=normal_fuente.render(' Normal ',False,(255,255,255),(200,200,100))
    n=True
    nn=False
    def normal():

        global v,bala_movy
        bala_movy = -1.2
        v=0.3
        return 10

    dificil_fuente=pygame.font.Font('FreeSansBold.ttf',50)
    dificil_texto=dificil_fuente.render(' Dificil ',True,(255,255,255),(200,200,100))
    d=True
    dn=False
    def dificil():
        global v,bala_movy
        bala_movy = -2
        v=0.4
        return 20


    running0=True
    running=True
    running1=True


    while running0:
        pantalla.blit(fondo_imagen,(0,0))
        #facil
        pantalla.blit(facil_texto,(150,120))
        #normal
        pantalla.blit(normal_texto, (550, 120))
        #dificil
        pantalla.blit(dificil_texto, (350, 320))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running0 = False
                running =False
                running1 =False

            if evento.type == pygame.MOUSEMOTION:
                if 150<evento.pos[0]<290 and 120<evento.pos[1]<185:
                    facil_texto = facil_fuente.render(' Facil ', True, (255, 255, 255), (0, 0, 0))
                    fn=True
                    if f:
                        sonido_clic()
                        f=False
                else:
                    facil_texto = facil_fuente.render(' Facil ', True, (255, 255, 255), (200, 200, 100))
                    f=True
                    if fn:
                        sonido_clic()
                        fn=False


                if 550<=evento.pos[0]<=750 and 120<=evento.pos[1]<=185:
                    normal_texto=normal_fuente.render(' Normal ',True,(255,255,255),(0,0,0))
                    nn=True
                    if n:
                        sonido_clic()
                        n=False
                else:
                    normal_texto = normal_fuente.render(' Normal ', False, (255, 255, 255), (200, 200, 100))
                    n = True
                    if nn:
                        sonido_clic()
                        nn=False

                if 350<=evento.pos[0]<=510 and 320<=evento.pos[1]<=385:
                    dificil_texto = dificil_fuente.render(' Dificil ', True, (255, 255, 255), (0, 0, 0))
                    dn=True
                    if d:
                        sonido_clic()
                        d=False
                else:
                    dificil_texto = dificil_fuente.render(' Dificil ', True, (255, 255, 255), (200, 200, 100))
                    d = True
                    if dn:
                        sonido_clic()
                        dn=False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if (150 < evento.pos[0] < 290 and 120 < evento.pos[1] < 185):
                    running0=False
                    enemigos_cantidad=facil()
                elif (550<=evento.pos[0]<=750 and 120<=evento.pos[1]<=185):
                    running0=False
                    enemigos_cantidad=normal()
                elif (350<=evento.pos[0]<=510 and 320<=evento.pos[1]<=385):
                    running0=False
                    enemigos_cantidad=dificil()
        pygame.display.update()

#------PERSONAJE--------
if True:
    pj_imagen=pygame.image.load('cohete.png')
    pj_posx=368
    pj_posy=526
    pj_movx=0
    pj_mostrar=True

#------ENEMIGOS----------
if True:
    enemigos_velocidad=random.choice([-v,v])
    enemigos_imagen = []
    enemigos_posx = []
    enemigos_posy = []
    enemigos_movx = []
    enemigos_mostrar= []

    for enemigo in range(enemigos_cantidad):
        enemigos_imagen.append(pygame.image.load('enemigo.png'))
        enemigos_posx.append(random.randint(0,536))
        enemigos_posy.append(random.randint(0,36))
        enemigos_movx.append(enemigos_velocidad)
        enemigos_mostrar.append(True)

#------BALA--------------
if True:
    bala_imagen=pygame.image.load('bala.png')
    bala_posx=-50
    bala_posy=-50
    bala_mostrar=False

#------COLISION----------
if True:
    def colision(x1,y1,x2,y2):
        d=math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
        if d<27:
            return True
        else:
            return False

#------PUNTAJE-----------
if True:
    puntaje=0
    texto_fuente=pygame.font.Font('FreeSansBold.ttf',40)
    texto_posx=5
    texto_posy=5

#------TERMINAR EL JUEGO---
if True:
    fin_sin_enemigos=[]
    for enemigo in range(enemigos_cantidad):
        fin_sin_enemigos.append(False)
    def fin():
        global running
        running=False

#------------LOOP DEL JUEGO-------------------------
if True:
    while running:
        #FONDO DE PANTALLA
        pantalla.blit(fondo_imagen, (0, 0))


        #MOSTRAR PUNTAJE
        texto = texto_fuente.render('Pts: {}'.format(puntaje), True, (255, 255, 255))
        pantalla.blit(texto,(texto_posx,texto_posy))

        #-----EVENTOS DEL JUEGO-----
        if True:
            for evento in pygame.event.get():
                #CERRAR EL JUEGO
                if evento.type == pygame.QUIT:
                    running=False
                    running2=False

                #AL PRESIONAR UNA TECLA
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        pj_movx=-0.4
                    if evento.key == pygame.K_RIGHT:
                        pj_movx=0.4

                    if evento.key == pygame.K_SPACE:
                        if not bala_mostrar:
                            sonido_disparo=pygame.mixer.Sound('disparo.mp3')
                            sonido_disparo.set_volume(0.2)
                            sonido_disparo.play()

                            bala_posx=pj_posx
                            bala_posy=pj_posy
                            bala_mostrar=True

                #AL SOLTAR UNA TECLAA
                if True:
                    if evento.type == pygame.KEYUP:
                        if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                            pj_movx=0

        # ---------PERSONAJE------------
        if True:
            if pj_mostrar:
                #MOVIMIENTO
                pj_posx+=pj_movx

                # LIMITE
                if pj_posx < 0:
                    pj_posx = 0
                if pj_posx > 736:
                    pj_posx = 736

                #IMPRIME PJ EN PANTALLA
                pantalla.blit(pj_imagen,(pj_posx,pj_posy))

        #----------BALA------------
        if bala_mostrar:
            #LIMITES
            if bala_posy <-64:
                bala_mostrar=False
            #MOVIMIENTO
            bala_posy+=bala_movy

            #MOSTRAR EN PANTALLA
            pantalla.blit(bala_imagen,(bala_posx+16,bala_posy+10))

        #----------ENEMIGO--------------
        if True:
            for enemigo in range(enemigos_cantidad):
                if enemigos_mostrar[enemigo]:
                    # MOVIMIENTO
                    enemigos_posx[enemigo] += enemigos_movx[enemigo]
                    # LIMITE
                    if enemigos_posx[enemigo] < 0:
                        enemigos_posx[enemigo] = 0
                        enemigos_posy[enemigo]+= 50
                        enemigos_movx[enemigo]*=-1
                    if enemigos_posx[enemigo] > 736:
                        enemigos_posx[enemigo] = 736
                        enemigos_posy[enemigo]+= 50
                        enemigos_movx[enemigo] *= -1

                    # IMPRIME ENEMIGO EN PANTALLA

                    pantalla.blit(enemigos_imagen[enemigo], (enemigos_posx[enemigo], enemigos_posy[enemigo]))

        # ----------COLISION--------
        if True:
            for enemigo in range(enemigos_cantidad):
                if enemigos_mostrar[enemigo]:
                    if colision(enemigos_posx[enemigo],enemigos_posy[enemigo],bala_posx,bala_posy):
                        bala_mostrar=False
                        bala_posy=pj_posy
                        puntaje+=1
                        enemigos_mostrar[enemigo]=False
                        colision_music = pygame.mixer.Sound('Golpe.mp3')
                        colision_music.set_volume(0.2)
                        colision_music.play()

                        #PARA AGREGAR VELOCIDAD SI ELEMINAS UNA NAVE ENEMIGA
                        '''for enemigo in range(enemigos_cantidad):
                            if enemigos_movx[enemigo]>0:
                                enemigos_movx[enemigo]+=0.1
                            elif enemigos_movx[enemigo]<0:
                                enemigos_movx[enemigo]-=0.1'''

        #-----------Fin--------------
        if True:
            for enemigo in range(enemigos_cantidad):
                if enemigos_posy[enemigo] > 462:
                    if  pj_posx<= enemigos_posx[enemigo] <=pj_posx+64 or pj_posx<= enemigos_posx[enemigo]+64 <=pj_posx+64:
                        pj_mostrar=False
                        bala_mostrar=False
                        for enemigo in range(enemigos_cantidad):
                            enemigos_mostrar[enemigo]=False
                        fin()

            if fin_sin_enemigos == enemigos_mostrar:
                fin()



        #ACTUALIZAR PANTALLA
        pygame.display.update()

#-----------LOOP MOSTRARA EL PUNTAJE FINAL----------
if True:
    puntae_final_fuente= pygame.font.Font('FreeSansBold.ttf',30)
    texto_final=puntae_final_fuente.render('PUNTAJE FINAL: {}'.format(puntaje),True,(255,255,255))

    running2=False
    virus=False
    while running1:
        pantalla.blit(fondo_imagen,(0,0))
        pantalla.blit(texto_final,(100,100))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running1=False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                running1=False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_k:
                    running2=True
                    running1=False

        pygame.display.update()


    #----------PARA KATHERINE------------------
    williams_imagen=pygame.image.load('amor1R.jpg')
    williams_corazon=pygame.image.load('williams_fondo.jpg')
    pantalla=pygame.display.set_mode((800,880))

    pygame.mixer.music.load('Te amo tanto.mp3')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)

    while running2:
        pantalla.blit(williams_corazon,(-249,-200))
        pantalla.blit(williams_imagen, (150, 220))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running2=False
                virus=True

        pygame.display.update()


if virus:
    for i in range(1):
        os.system('start amor.bat')


#CERRAR EL INIT
pygame.quit()

#---MEDIR EL TIEMPO DE EJECUCION---
final=time.time()
duracion_tiempo= math.ceil(final-inicio) if (final-inicio) % 1 >0.5 else math.floor(final-inicio)


