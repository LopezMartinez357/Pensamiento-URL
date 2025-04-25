import time

def adivina_el_numero(numero, intentos, tiempo_inicio):
    if intentos == 0:
        print("¡Te has quedado sin intentos! El número era:", numero)
        return

    try:
        intento = int(input(f"Tienes {intentos} intento(s) restante(s). Ingresa tu número: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        adivina_el_numero(numero, intentos, tiempo_inicio)
        return

    if intento == numero:
        tiempo_final = time.time()
        tiempo_total = tiempo_final - tiempo_inicio
        print(f" ¡Felicidades! Adivinaste el número {numero} en {round(tiempo_total, 2)} segundos.")
        return
    elif intento < numero:
        print("Demasiado bajo.")
    else:
        print("Demasiado alto.")

    adivina_el_numero(numero, intentos - 1, tiempo_inicio)


import random
numero_secreto = random.randint(1, 100)  
print("Bienvenido al juego de Adivina el Número.")
print("Elige un número entre 1 y 100.")
print("¡Buena suerte!")

tiempo_inicio = time.time()
adivina_el_numero(numero_secreto, 5, tiempo_inicio)
