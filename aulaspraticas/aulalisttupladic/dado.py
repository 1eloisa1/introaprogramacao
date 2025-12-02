"""Escreva um programa em Python que simule o lançamento de um dado � vezes e imprima
o percentual de surgimento de cada face do dado. O valor � é introduzido pelo usuário.
Seu programa deverá utilizar uma lista para armazenar os números de aparecimento de
cada face. Dica: A função randint(ini, fim) do pacote random gera números
aleatórios no intervalo """
import random
nrolagens=int(input("numero de rolagens do dado: "))
c=[0,0,0,0,0,0]
for i in range(nrolagens):
    f=(random.randint(1, 6))
    c[f-1]+=1
for i in range (6):
    p=c[i]/nrolagens*100
    print(f"face {i+1}:{c[i]} vezes({p:.2f}%)")

print(c) 
