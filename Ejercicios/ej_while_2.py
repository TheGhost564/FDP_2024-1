# Ejemplo while 2.
# Autor: Sebastian Duarte Mera. Cod: 2421811-2725
# Fecha: 08/04/2024

continuar = "s"
total = 0
articulos = 0


while (continuar == "s") or (continuar == "S"):

    cantidad = int(input("Ingrese la cantidad a sumar. "))
    total += cantidad
    print("Total= ", total)
    continuar = input("Continuar suma? s / n")
    print("Artiulos: ", articulos)
    articulos += 1