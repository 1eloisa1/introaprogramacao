pessoas = 4

alturas = []   
sexos = []     

for i in range(pessoas):
    a = float(input(f"Altura da pessoa {i+1}: "))
    s = input(f"Sexo da pessoa {i+1} (M/F): ")
    alturas.append(a)
    sexos.append(s)

maior = alturas[0]
menor = alturas[0]
sexomaior = sexos[0]
sexomenor = sexos[0]

for i in range(pessoas):
    if alturas[i] > maior:
        maior = alturas[i]
        sexomaior = sexos[i]
    if alturas[i] < menor:
        menor = alturas[i]
        sexomenor = sexos[i]

soma_f = soma_m = 0
mulher = homem = 0

for i in range(pessoas):
    if sexos[i] == "F":
        soma_f += alturas[i]
        mulher += 1
    elif sexos[i] == "M":
        soma_m += alturas[i]
        homem += 1

mediaaltf = soma_f / mulher
mediaaltm = soma_m / homem 

print(f"\nAlturas: {alturas}")
print(f"Sexos: {sexos}")
print(f"Maior altura: {maior} (sexo {sexomaior})")
print(f"Menor altura: {menor} (sexo {sexomenor})")
print(f"Média altura Feminino: {mediaaltf:.2f}")
print(f"Média altura Masculino: {mediaaltm:.2f}")
print(f"Total Mulheres: {mulher}, Total Homens: {homem}")