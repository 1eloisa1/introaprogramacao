"""Faça um programa que leia números repetidamente até que o valor -1 seja digitado.
Quando isso ocorrer, o programa deve exibir o menor valor, o maior valor e a soma dos
valores."""

nun1=int(input("Digite um numero:"))
soma=0
maior=menor=nun1
while (nun1!=-1):
    soma=soma+nun1
    if(nun1>maior):
        maior=nun1
    if(nun1<menor):
        menor=nun1
    nun1=int(input("Digite um numero:"))
print(f"O maior numero é: {maior}, o menor é {menor} e a soma {soma}")