#Programa que detecta los números pares entre 1 y n.
#Autor: Sebastian Duarte Mera. Cod: 2421811
#Fecha: 1/04/2024

contador = 0

n = int(input("Digite un número entero, por favor. "))

for i in range (1, n):
    if (i % 2 == 0):
        contador = contador + 1
        
print("Entre 1 y ", n, " hay ", contador, "pares")