# Adivinar un numero en un rango específico creado por la PC | Enunciado: Adivina un numero entre 1 y 10
# diremos si es mayor | menor | igual al creado por la PC
import random


def adivina_el_num(num):
    print("==================================")
    print("Bienvenido al juego!")
    print("==================================")
    print("Tu objetivo es adivinar el número generado por la IA.")
    
    numero_aletorio = random.randint(1, num) # num aleatorio entre 1 y num

    prediccion = 0

    while prediccion != numero_aletorio:
        prediccion = int(input(f"Adivina un número entre 1 y {num}: "))
        if prediccion < numero_aletorio:
            print("Intenta otra vez. Este número es pequeño.")
        elif prediccion > numero_aletorio:
            print("Intenta otra vez. Este número es muy grande.")
    print(f"Felicitaciones! Adivinaste el número {num} correctamente!")


adivina_el_num(10)