#Faça um programa que leia um valor inteiro positivo n e determina a soma dos n primeiros números pares positivos (utilize o comando for).

n=int(input('digite um numero: '))
soma=0
for i in range(1, n+1):
    soma+=i*2
    print(soma)