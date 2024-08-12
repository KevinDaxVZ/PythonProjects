#!/bin/bash
#AUTHOR: Kevin Dax Victorio Zanabria

#py3 por que necesitamos pip
#yt-dlp esta herramienta nos permite descargar videos de listas
#ffmpeg nos permite descargar maxima calidad de video y audio de los videos
#Ejecutalo con sudo por si no tienes las librerias instaladas de python.
#Ejemplo:  sudo ./download_playlist_youtube_v2.sh


which python3
if [ $? != 0 ]; then sudo apt install python3 -y ; fi
clear

which yt-dlp
if [ $? != 0 ]; then pip install yt-dlp ; fi
clear

which ffmpeg
if [ $? != 0 ]; then sudo apt install ffmpeg -y ; fi
clear

read -p 'Ingrese la URL: ' URL

opcion=0
mensaje=false
opciones=(1 2 3)


while [[ ! " ${opciones[@]} " =~ " $opcion " ]] ; do

        clear
        if [ $mensaje == 'true' ]; then echo "ERROR... LAS OPCIONES SON 1 2 3" ; fi

        echo "-----Elija la calidad-----"
        echo "1.[480]"
        echo "2.[720]"
        echo "3.[1080]"
        read -p "opcion: " opcion

        mensaje=true

done


calidades=([1]=480 [2]=720 [3]=1080)
calidad=${calidades[opcion]}

clear
echo -e "***********DESCARGANDO**********\n\t-CALIDAD=$calidad\n\tURL=$URL  "
yt-dlp -f "bestvideo[height<=?$calidad]+bestaudio/best[height<=?$calidad]" "$URL" 2>/dev/null

wait
echo "Descarga completada."
