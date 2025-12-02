"""Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro
número elevado ao segundo número. Não utilize a função de potência da linguagem. """

b=int(input("Número para a Base: "))
e=int(input("Número para o Expoente: "))
p=1
for i in range(e):
    p*=b
print(p)
