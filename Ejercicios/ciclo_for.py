#Programa que imprime los números desde 1 hasta n.
#Autor: Sebastian Duarte Mera.
#Codigo: 2421811-2725
#Fecha: 01/04/2024.

#n = int(input("Por favor, digita un numero mayor a 10 "))

#if (n >= 10):
    #for i in range (n, 1, -1):
        #print(i)
    
#else:
    #print("Digita un número valido, por favor.")

#Número de repeticiones del bucle (Contadores)
    
#a = 0

#for i in range (0, 5, 2):
    #a = a + 1
    
#print("El valor de a es: ", a)

n = int(input("..."))

if (n <= 20):
    for  i in range (1, n + 1):
        factorial = 0
        for j in range (1, i + 1):
            factorial += j
            
        respuesta = "El factorial de ", i, "es:", factorial
        print(respuesta)
        
else:
    respuesta="mayor que 20"
    print(respuesta)        