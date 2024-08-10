#DOWNLOAD INSTAGRAM PROFILE / DESCARGAR PERFIL DE INSTAGRAM
#PROBANDO EN EQUIPOS WINDOWS, CON PYTHON 3.10
#SE NECESITA INSTALAR REQUESTS, BS4

import os
import subprocess
import requests
import bs4

def found_url(bs):
    meta_tag = bs.find('meta',
                       content=lambda value: value and 'https://scontent-hou1-1.cdninstagram.com' in value)

    url_imagen = meta_tag.get('content')
    comando = ['curl', '-o',nombre, url_imagen]

    print('Descargando... POR FAVOR ESPERE...')
    with open(os.devnull, 'wb') as nul:
        subprocess.run(comando, stderr=nul, stdout=nul, check=True)

def respuesta_servidor(url):
    response = requests.get(url)

    if response.status_code == 200:
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        found_url(bs)

    else:
        print('El servidor no esta respondiendo... Intentelo otra vez')


def depurando_url(url):
    url = url.lstrip()
    url = url.rstrip()

    global nombre
    nombre = url.split('/')[-2]
    nombre = nombre+'.jpg'

    respuesta_servidor(url)


#OPCIONES
def opcion(opc,target):
    if opc == '1':
        if '@' in target:
            target = target.split('@')[1]

        url = 'https://www.instagram.com/'+target+'/'

        depurando_url(url)

    elif opc == '2':
        url = target
        depurando_url(url)

    else:
        print('El formato es erroneo')



if __name__ == '__main__':
    print('Esta aplicacion descarga la foto de perfil de una cuenta de instagram')
    print('OPCIONES VALIDAS: [@username] [username] [URL/TARGET]')
    target = input('Ingrese el target: ')


    if '@' in target:
        opc = '1'

    elif 'https' not in target and '@' not in target:
        opc = '1'

    elif 'https' in target and '@' not in target:
        opc = '2'

    else:
        opc = '0'

    opcion(opc,target)


