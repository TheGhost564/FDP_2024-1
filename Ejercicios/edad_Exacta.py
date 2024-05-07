# Programa que pide la edad en años y la muestra en años, meses y dias
# Autor: Sebastian Duarte Mera Cod: 2421811-2725, Santiago Valdivieso Aragon Cod: 2416671-2725
# Fecha: 11/03/2024

nombre = input("Ingrese su nombre: ")
year_Today = int(input("Ingrese el año actual: "))
month_Today = int(input("Ingrese el mes actual: "))
day_Today = int(input("Ingrese el dia actual: "))
year = int(input("Ingrese su año de nacimiento: "))
month = int(input("Ingrese su mes de nacimiento: "))
day = int(input("Ingrese su dia de nacimiento: "))

years = year_Today - year - ((month_Today, day_Today) < (month, day))
dif_Months = month_Today - month
dif_days = day_Today - day

months = (dif_Months + 12.17 * (dif_Months < 0)) % 12.17
days = (dif_days + 30.41 * (dif_days < 0)) % 30.41

print("Hola ", nombre, ", tienes ", years, " años, ", months, " meses y ", days, " dias.")
