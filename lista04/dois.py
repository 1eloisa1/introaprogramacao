"""Faça um programa que leia números repetidamente até que o valor -1 seja digitado.
Quando isso ocorrer, o programa deve exibir o menor valor, o maior valor e a soma dos
valores. 
"""
nun=int(input("digite um numero: "))
maior=nun
menor=nun
soma=0
while nun!=-1:
    soma+=nun
    if nun<menor:
        menor=nun
    if nun>maior:
        maior=nun
    nun=int(input("digite um numero: "))
print(f"maior é: {maior}, menor é: {menor} e a soma de tudo é: {soma}")