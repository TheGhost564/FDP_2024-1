# 
# Autor: Sebastian Duarte Mera. Cod: 2421811-2725
# Fecha: 08/04/2024

n = int(input("Por favor, digite un numero entero. "))

pares = 0

for i in range (1, n + 1):
    suma = 0
    
    for j in range (1, i + 1):
        suma += j
    
    if (i % 2 == 0):
        pares = pares + 1
        
        
print("Entre 1 y ", n, " hay un resultado de suma de ", suma, "y ", pares, "pares.")