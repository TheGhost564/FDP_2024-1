# Salario neto.
# Autor: Sebastian Duarte Mera. Cod: 2421811-2725
# Fecha: 11/03/2024

cc = input("Digita tu número de cedula, por favor ")
salario_Basico = int(input("Digite su salario, por favor "))
year = int(input("Digite su año de vinculación,  por favor "))

if ((salario_Basico > 1200000) and (year > 1990)):
    salario_Neto = salario_Basico - salario_Basico * 0.08

else:
    if ((salario_Basico < 550000) or (year == 1990)):
        salario_Neto = salario_Basico - salario_Basico * 0.02

    else:
        salario_Neto = salario_Basico - salario_Basico * 0.05

print(cc, " Su salario es: ", salario_Neto)
