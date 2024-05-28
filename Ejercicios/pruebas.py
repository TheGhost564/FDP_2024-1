notas = [[3.5, 4.0, 4.9, 3.2], [1.8, 5.0, 3.0, 2.5], [4.5, 3.5, 4.0, 2.0]]
numfilas = len(notas)
numcols = len(notas[0])
acumi = 0
acumj = 0
sumar = 0


for i in range(numfilas):
    for j in range(numcols):
        sumar += notas[i][j]
    
print(round(sumar))