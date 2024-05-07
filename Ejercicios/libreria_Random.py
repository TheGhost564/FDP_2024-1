#Programa que pide la edad en años y la muestra en meses
#Autor: Sebastian Duarte Mera 2421811
#29/04/2024

import random

print("Funcióń random()")
print(random.random())

print("Funcióń randrange(start, stop, step), sin incluir el limite superior")
for i in range(1, 10):
    print(random.randrange(1, 7))

print("Funcióń randint(start, stop), incluye el limite superior")
for i in range(1, 10):
    print(random.randint(1, 6))
    
print("Funcióń uniform(start, stop), genera número decimales incluyendo el limite superior")
for i in range(1, 10):
    print(random.uniform(1, 6))
    
print("Funcióń choice([a, b, c]), escoge un elemento aleatorio de la lista")
for i in range(1, 10):
    lista = [3, 9, 26, 44, 85]
    print(random.choice(lista))