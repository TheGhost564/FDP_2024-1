# variable = [[dato1, dato2,], [dato3, dato4]]
nombres = [["Oscar Mario", "Gomez",],
            ["Juan José", "Perez"],
            ["Jhon Jairo", "Yepes"]]


# Imprime el arreglo print(variables)
print(nombres)

# Imprime la segunda fila print(variable[])
print(nombres[1])

# Imprimir el primer elemento print(variable[fila][columna])
print(nombres[2][1])

# Crear lista con valores nulos
# variable = []
# for i in range(filas):
    #variable.append([None]*columnas)
    
# Cambiar dato variable[fila][columna] ="dato0"

# Agregar datos a un arreglo vacio
nombres1 = []
filas = int(input("Filas: "))

for i in range(filas):
    nom = input("Nombre: ")
    ape = input("Apellido: ")
    nombres1.append([nom, ape])
    
print(nombres1)

agregar = "S" 

while (agregar == "S") or (agregar == "s"):
    nom = input("Nombre: ")
    ape = input("Apellido: ")
    nombres1.append([nom, ape])
    agregar = input("Desea agregar otro? s / n ")
    
# Imprimir valores por separado i almacena la fila
# for i in arreglo:
for i in nombres:
    print("Nombre: ", i[0], "Apellido", i[1])

#Igual que arriba i almacena el primer valor de la fila, j el segundo :  for i, j in arreglo:
for i, j in nombres:
    print(i, j)