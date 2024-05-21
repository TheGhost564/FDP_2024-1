# Primer ejercicio de Python con arreglos.
# Autor: Sebastian Duarte Mera 2421811-2725
# 20/05/2024

import math

notas = [4, 3, 0, 2, 1, 3, 2, 4, 5, 5]
suma = 0

for numero in notas:
    suma += numero
    
promedio = suma / len(notas)
print("El promedio es: ", promedio)
print("El mayor valor es: ", max(notas))
print("El menor valor es: ", min(notas))