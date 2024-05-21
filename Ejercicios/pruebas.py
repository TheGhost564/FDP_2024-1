import math

notas = [4, 3, 0, 2, 1, 3, 2, 4, 5, 5]
numero_n = len(notas)

suma = 0

for numero in notas:
    suma += numero
    
promedio = suma / numero_n
    
print(promedio)