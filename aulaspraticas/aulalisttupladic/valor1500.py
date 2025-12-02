"""2 Faça um programa que crie uma lista com os valores de 1 a 500 e depois imprima os
elementos dessa lista na vertical usando outro laço."""

lista=[]
for i in range (1, 501):
    lista.append(i)
for i in range (len(lista)+1):
    if i>0:
        print(i)
