# Programa que permite calcular el salario neto de un trabjador
# Autores: Carlos Muñoz Cod: 2417374, Sebastian Duarte Cod: 2421811
# Fecha: 18/03/2024

cc = input("Digite su numero de cedula (sin puntos). ")
smmlv = int(input("Digite su salario. "))

if smmlv < 2300000:
    salud_Pension = smmlv * 0.08
    des_syp = smmlv - salud_Pension
    salario_Neto = des_syp + 162000
    
    print("Señor", cc, "Salario Basico:    ", smmlv, "\nDescuentos por salud y pensión:    ", des_syp, "\nSalario Neto: ", salario_Neto)
   
   
elif smmlv >= 5200000:
    desc = smmlv * 0.09
    salario_Neto = smmlv - desc
    
    print("Señor ", cc, "Salario Basico:    ", smmlv, "\nDescuentos por fondo de solidaridad, salud y pensión:    ", desc, "\nSalario Neto: ", salario_Neto)
    
else:
    print("Salario fuera de parametros.")