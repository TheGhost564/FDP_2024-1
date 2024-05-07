# Primer programa de Python con arreglos.
# Autor: Sebastian Duarte Mera 2421811-2725
# 06/05/2024

lista = [1.5, 2.0, 1.8]
print(lista)
print(lista[0])
lista_1 = []
# se utiliza None para crear las posiciones a utilizar
lista_2 = [None] * 4
print(lista_2)

arreglo = []
arreglo.append(10)
arreglo.append(20)
arreglo.append(30)

print("Datos del arreglo")
print(arreglo)

#razas.append("galgo")
#razas.append("podenco")
#razas.append("criollo")
#razas.append("chihuahua")
#razas.append("bulldog")

# Ingrese 4 razas de perro.
razas = []
for i in range (0,4):
    r = input("Escribe una raza de perro")
    razas.append(r)
print(razas)

#todas las razas de gato que recuerde el usuario.
razas_G = []
continuar = "s"
while (continuar == "s") or (continuar == "S"):
    g = input("Escribe una raza gatuna. ")
    razas_G.append(g)
    continuar = input("¿Desea continuar? s/n")    
print(razas_G)

#todas las razas de gato que recuerde el usuario si la varible continuar.
razas_G = []
while True:
    g = input("Escribe una raza gatuna. ")
    razas_G.append(g)
    continuar = input("¿Desea continuar? s/n")   
    if continuar != "s" or "S":
        break
print(razas_G)

# variable.insert (posicion, texto a insertar)
