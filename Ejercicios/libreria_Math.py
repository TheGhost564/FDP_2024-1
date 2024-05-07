# Ejemplo de uso de la libreria Math.
# Autor: Sebastian Duarte Mera, Cod: 2421811-2725.
# Fecha: 15/04/2024.

#Importar libreria.
import math

a = -5
b = 3.46464
base = 2
c = math.sqrt(base)
c_2 = round(math.sqrt(base), 2)
exp = 7
valor_abs_a = abs(a)
int_b = round(b)
int_c = round(c)

n1 = "Petro"
n2 = "Pedro"
n3 = "Peter"


# Función abs (valor absoluto).
print("el valor absoluto de ", a, "es: ", abs(a))


# Funciones ceil y floor (regresará el siguiente entero y regresará elentero anterior respectivamente).
print("Ceil de ", b, "es ", math.ceil(b))
print("Floor de ", b, "es ", math.floor(b))


# Función Round, round(valor, # de decimales a utilizar).
print("Round de ", b, "es ", round(b))
# Round con 2 decimales.
print("Round de ", b, "es ", round(b, 2))


# Función pow (potencia), pow(base, exponente).
print("La potencia ", exp, "de ", base, "es ", math.pow(base, exp))


# Función de raiz cuadrada, math.sqrt(valor).
print("La raiz cuadrada de ", base, "es ", math.sqrt(base))


# Raiz cuadrada de 2 redondeada con 2 decimales.
print("La raiz cuadrada redondeada de ", base, "es ", c_2)
# Raiz cuadrada de 2 redondeada con 2 decimales anidada.
print("La raiz cuadrada redondeada de ", base, "es ", round(math.sqrt(base), 2))


# Valor maximo de un conjunto de números, max(valor1, valor2,..., valorn)
print("El valor maximo entre: ", a, b, c, "es ", max(a, int_b, int_c))

print("Valor absoluto maximo entre: ", a, b, c, "es ", max(valor_abs_a, abs(round(int_b)), abs(int_c)))

print("El valor maximo entre ", n1,",", n2,",", n3, "es ", max(n1, n2, n3))


# Valor minimo de un conjunto de números, min(valor1, valor2,..., valorn)
print("El valor minimo entre: ", a, b, c, "es ", min(a, int_b, int_c))

print("Valor absoluto minimo entre: ", a, b, c, "es ", min(valor_abs_a, abs(round(int_b)), abs(int_c)))

print("El valor minimo entre ", n1,",", n2,",", n3, "es ", min(n1, n2, n3))


# Número π, math.pi.
print("El número π es ", math.pi)