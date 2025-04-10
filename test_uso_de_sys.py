#!/usr/bin/python

from colorama import Fore
import sys

"""
3. Desarrolle un programa que permita al usuario ingresar sus datos personales: 
Nombre, Edad, Altura (en metros), Peso (en kgs) y Correo Electrénico 

 El programa debe realizar lo siguiente: 

 Verificar si la persona es mayor de edad (18 afios 0 mas) 
 Determinar si la altura ingresada es mayor a 1.75 metros 
 Confirmar si el peso ingresado es menor o igual a 80 kgs 
 Validar si el correo ingresado contiene “@”
"""

class Persona:
    def __init__(self,nombre,edad,altura,peso,correo):
        self.nombre = nombre
        self.edad = int(edad)
        self.altura = float(altura)
        self.peso = float(peso)
        self.correo = correo

    def __str__(self):
        return f"{Fore.RESET}Hola Soy {self.nombre}, estos fueron algunos datos mios"

def menu_uso():
    print("[HELP] ")
    print("\tUSE\t.\\script.py -name [nombre] -edad [edad] -altura [altura] -peso [peso] -correo [correo]")
    print()
    print("[VARIABLES]")
    print("\t-nombre\t 'Nombre de la persona'")
    print("\t-edad\t 'edad de la persona'")
    print("\t-altura\t 'altura de la persona'")
    print("\t-peso\t 'peso de la persona'")
    print("\t-coreo\t 'correo de la persona'")
    exit()

if __name__ == "__main__":
    if len(sys.argv[1:]) != 10:
        menu_uso()

    variables = {1:"-nombre",2:"-edad",3:"-altura",4:"-peso",5:"-correo"}

    for i in range(1,6):
        if variables[i] != sys.argv[i*2-1]:
            menu_uso()

    persona = Persona(*[sys.argv[i] for i in range(2,11,2)])

    print()
    print(f"***** INFORMACION DE {persona.nombre} ******")
    print(f"{Fore.GREEN if persona.edad >= 18 else Fore.RED}¿{persona.nombre} es mayor de edad? {persona.edad >= 18}")
    print(f"{Fore.GREEN if persona.altura >= 1.75 else Fore.RED}¿{persona.nombre} supera los 1.75 metros? {persona.altura >= 1.75}")
    print(f"{Fore.GREEN if persona.peso >= 80 else Fore.RED}¿{persona.nombre} pesa mas que 80 kgs? {persona.peso >= 80}")
    print(f"{Fore.GREEN if "@" in persona.correo else Fore.RED}¿el correo de {persona.nombre} tiene algun @ ? {"@" in persona.correo}")

    print()
    print(persona)
