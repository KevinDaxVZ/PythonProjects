#TENGO UNA VERSION 2 DE ESTE SCRIPT, EL CUAL SI DESCARGA EN LA CALIDAD MAS ALTA LOS VIDEOS DE YOUTUBE, ESTA SOLO LOS DESCARGA POR LO GENERAL EN UNA CALIDAD ESTANDAR
#REVISA MI VERSION 2

sudo apt install python3 -y 
pip install yt-dlp
sudo apt install ffmpeg -y



#yt-dlp -f 'bestvideo[height<=?1080]+bestaudio/best[height<=?1080]' 'https://www.youtube.com/watch?v=5O1srQNyJXo&list=PLWtYZ2ejMVJmUTNE2QVaCd1y_6GslOeZ6&index=1&pp=iAQB'

echo -e '\t*****¡ATENCION!****'
echo -ne "Los videos se descargar en el directorio actual en el que estas$(pwd)\n"
read -p 'Ingrese la URL de tu playlist: '
yt-dlp -f 'bestvideo[height<=?1080]+bestaudio/best[height<=?1080]' "$REPLY"


