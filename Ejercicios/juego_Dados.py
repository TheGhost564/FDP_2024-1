# Juego de dados.
# Autores: Sebastian Duarte Cod: 2421811, Carlos Andres Muñoz Cod: 2417374
# 29/04/2024

import random

numero = 0
puntos = 5000
confirm = "s"
win = 0
lost = 0

while (puntos >= 500) and ((confirm == "s") or (confirm == "S")):
    num_Ran = random.randrange(1, 7)
    numero = int(input("Digite un número del 1 al 6. "))
    if puntos >= 500:
        if num_Ran == numero:
            win += 1
            puntos += 1000
            print("El número genarado es: ", num_Ran, "Haz ganado, \n¡FELICITACIONES!")
            print("Tu puntaje es: ", puntos)
        else:
            lost += 1
            puntos -= 500
            print("El número genarado es: ", num_Ran, "Te ¡PELARON!")
            print("Tu puntaje es: ", puntos)
        confirm = input("¿Deseas continuar? S/N ")
else:
    print("Haz ganado ", win, " veces.", "\nTe PELARON ", lost, " veces.")