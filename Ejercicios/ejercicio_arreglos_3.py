# Arreglos bidimensional.
# Autor: Sebastian Duarte Mera. Cod: 2421811-2725
# Fecha: 27/05/2024

jogadores = []

jogadores.append(["Manuel Neuer", "Camiseta #1", "Posición: Portero"])
jogadores.append(["Eric Dier", "Camiseta #15", "Posición: Defensa"])
jogadores.append(["Matthijs de Ligt", "Camiseta #4", "Posición: Defensa"])
jogadores.append(["Dayot Upamecano", "Camiseta #2", "Posición: Defensa"])
jogadores.append(["Aleksandar Pavlović", "Camiseta #45", "Posición: Centrocampista"])
jogadores.append(["Konrad Laimer", "Camiseta #27", "Posición: Centrocampista"])
jogadores.append(["Alphonso Davies", "Camiseta #19", "Posición: Centrocampista"])
jogadores.append(["Leon Goretzka", "Camiseta #8", "Posición: Mediocampista"])
jogadores.append(["Joshua Kimmich", "Camiseta #6", "Posición: Centrocampista"])
jogadores.append(["Mathys Tel", "Camiseta #39", "Posición: Delantero"])
jogadores.append(["Thomas Müller", "Camiseta #25", "Posición: Delantero"])

print("Plantilla ultimo partido Bayern Múnich", "\n", jogadores)

for i in jogadores:
    print("Jogador: ", i[0], "|| ", i[1], "|| ", i[2])