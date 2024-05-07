# Programa que calcula el promedio general de la asiganutar FDP.
# Autores: Sebastian Duarte Mera. Cod: 2421811-2725, Juan Camilo Ramirez Urbano. Cod: 2418301-2725
# Fecha: 08/04/2024

# Definimos las variables a utilizar.
continuar = "s"

p1 = 0
p2 = 0
lab = 0
trabajo_Final = 0
definitiva = 0
total_Notas = 0

cantidad_Estudiantes = 0

# Iniciamos la estructura while, donde se repetira siempre y cuando continuar es igual a s o S.
while (continuar == "s") or (continuar == "S"):
    
    cantidad_Estudiantes += 1
    
    p1 = float(input("Escribe la nota del parcial 1. "))
    p2 = float(input("Escribe la nota del parcial 2. "))
    lab = float(input("Escribe la nota del laboratorio. "))
    trabajo_Final = float(input("Escribe la nota del trabajo final. "))
    
    definitiva = (p1 * 0.30) + (p2 * 0.35) + (lab * 0.25) + (trabajo_Final * 0.10) // 1
    total_Notas += definitiva
    
    promedio_general = total_Notas // cantidad_Estudiantes
    
    print("El promedio del estudiante # ", cantidad_Estudiantes, " es: ", definitiva)
    print("El promedio general del grupo es: ", promedio_general)
        
    continuar = input("Desea continuar? s / n")
    
