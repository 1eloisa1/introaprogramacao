""") Crie um programa para gerar uma matriz de dimensões 3x3 preenchida com valores
informados pelo usuário. Além disso, o programa deverá solicitar que o usuário digite um
valor e irá verificar se ele pertence à matriz. """

m=[[None]*3 for i in range(3)]

for i in range(3):
    for l in range(3):
        m[i][l]=int(input(f"o elemneto {i} {l}: "))

veri=int(input("verificar? "))
for i in range(len(m)):
    for l in range(len(m)):
        ver=m[i][l]
        if veri==ver:
            print(f"esta na matrizna linha {i} e coluna {l}")
        else:
            print(f"nao esta na linha {i} e coluna {l}")