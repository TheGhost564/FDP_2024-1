import string

num_1 = 20
num_2 = 5
n1 = "Pedro"
n2 = "Alexandra"
n3 = "    Pedro    "
n4 = "    MArTiNEZ    "

# Función str, convierte el dato establecido en una cadena de caracteres, str(valor númerico)
print(str(num_1))


# Función len, indica la longitud (cantidad de caracteres), len(Cadena de Caracteres)
print(n1, "tiene", len(n1))
print(n3, "tiene", len(n3))


# Función lower, convierte la Cadena de Caracteres a minuscula, Variable de la Cadena.lower()
print(n2, "en minusculas", n2.lower())


# Función upper, convierte la Cadena de Caracteres a mayuscula, Variable de la Cadena.upper()
print(n2, "en mayusculas", n2.upper())


#Función strip, quita los espacios al comienzo y al final de la cadena, Variable de la Cadena.strp()
print(n3, "sin espacios tiene", len(n3.strip()), "caracteres")


# Función title, deja la primera letra en mayuscula y las siguientes en minusculas, Variable de la Cadena.title()
print(n4, "en formato title es ", n4.strip().title())


# Función index, retoma la posicon de la primera ocurrecia de busqueda de izquierda a derecha, Variable de la Cadena.index(Caracter a buscar)
print(n1.index("P") )


# Función count, cuantas cuantas veces de apariciones de una subcadena dentro de una cadena, Variable de la Cadena.count(subcadena)
print(n1.count("d"))