#Programa que imprime los multiplos de 3 en una serie 1 a n.
#Autor: Sebastian Duarte Mera, Cod: 2421811.
#Fecha: 01/04/2024.

contador = 0

n = int(input("Digite un número entero, por favor. "))

for i in range (1, n):
    if (i % 3 == 0):
        contador = contador + 1
        
print("Entre 1 y ", n, " hay ", contador, "multiplos.")