
import random
nrolagens = int( input("Número de Rolagens do Dado: ") )
c = [0,0,0,0,0,0]
total = 0
while nrolagens != 0:
    for i in range(nrolagens):
        f = (random.randint(1, 6))
        c[f-1] += 1
        total += 1

    print("Resultados:")
    for i in range (6):
        p = c[i]/total*100
        print(f"face {i+1}: {c[i]} vezes({p:.2f}%)")

    nrolagens = int( input("Número de Rolagens do Dado: ") )

print("Fim de Programa")