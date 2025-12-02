"""Numa eleição existem três candidatos. Faça um programa que peça o número total de
eleitores, leia os votos consistindo nos números dos candidatos (você define tais números)
e, ao final, exiba o número de votos de cada um recebeu. """


eleitores=int(input("Número de Eleitores: "))
c1=0
c2=0
c3=0
for i in range (eleitores):
    voto=int(input(f"Seu Voto? Eleitor {i+1}: "))
    if voto==1:
        c1+=1
    elif voto==2:
        c2+=1
    elif voto==3:
        c3+=1
    else:
        print("Número não Válido")
print(f"Candidato 1 teve {c1} votos; \nCandidato 2 teve {c2} votos; \nCandidato 3 teve {c3} votos.")