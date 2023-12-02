# Adivinar un numero en un rango específico creado por la PC | Enunciado: Adivina un numero entre 1 y 10
# diremos si es mayor | menor | igual al creado por la PC
import random

def adivina_el_num(num):
    print("==================================")
    print("Bienvenido al juego!")
    print("==================================")
    print("Tu objetivo es adivinar el número generado por la IA.")
    
    numero_aletorio = random.randint()
    