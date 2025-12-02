"""Escreva um programa que leia dois números e imprima o resultado da divisão inteira do
primeiro pelo segundo, assim como o resto da divisão, usando o comando while e o
operador aritmético de subtração. Lembre-se que podemos entender o quociente da
divisão de dois números como a quantidade de vezes que podemos retirar o divisor do
dividendo. Logo, 20 ÷ 4 = 5, pois podemos subtrair 4 cinco vezes de 20. """

divid=int(input("digite um numero: "))
divis=int(input("digite um numero: "))
quociente=0
rest=divid
while rest>=divis:
    rest-=divis
    quociente+=1

print(f"o resto é: {rest} e o resultado é: {quociente}")