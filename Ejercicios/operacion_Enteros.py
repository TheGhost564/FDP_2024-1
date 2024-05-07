# Programa que lee dos numeros entreros y hace la operación escogida por el usuario.
# Autores: Sebastian Duarte Cod: 2421811, Carlos Andres Muñoz Cod: 2417374
# 18/03/2024

num_1 = int(input("Digita el primer número entero, por favor. "))
num_2 = int(input("Digita el segundo número entero, por favor. "))
opcion = int(input("Digita el número de la operación que quieres realizar. \n1: Suma \n2: Resta \n3: Multiplicación \n4: División. "))

result = 0
opera = ""
if (opcion == 1):
    result = num_1 + num_2
    opera = "Suma"
elif (opcion == 2):
    result = num_1 - num_2
    opera = "Resta"
elif (opcion == 3):
        result = num_1 * num_2
        opera = "Multiplicación"
elif (opcion == 4):
    opera = "División"
    if (num_2 == 0):
        print("No se puede operar por / 0")
    
    else:
        result = num_1 / num_2
        
else:
    print("No es una opción valida")
    
if result:
    print("Operación ", opera, "El resultado es: ", result)