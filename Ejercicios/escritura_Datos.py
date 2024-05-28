# variable = open("nombre_de_archivo.txt", "w") "w" = write, "a" = append, "r" = read 

archivo = open("marcas_Carro.csv", "w")

macar = []
for i in range(10):
    macar.insert(input("10 marcas de carro: "))
    
print(macar)



