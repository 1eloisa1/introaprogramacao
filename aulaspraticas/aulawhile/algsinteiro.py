"""Escreva um programa para determinar o número de algarismos de um número inteiro
positivo dado."""

nun1=int(input("digite um numero:"))
contador=1
if(nun1>0):
    while (nun1//10!=0):
        nun1=nun1//10
        contador=contador+1
        #print(contador)
else:
    print("digite um numero maior que zero")
   
print(f"o numero dighitado tem {contador} algarismos")