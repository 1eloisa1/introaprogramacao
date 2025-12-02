"""Escreva um programa que leia como entrada os três lados de um triângulo, classifique o triângulo em equilátero, isósceles ou escaleno, 
e exiba na tela sua classificação.
Dicas:
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes.
"""
lado1 = float(input("Digite o 1° lado: "))
lado2 = float(input("Digite o 2° lado: "))
lado3 = float(input("Digite o 3° lado: "))

if (lado1 == lado2 == lado3):
    print("O triangulo é equilatero")
elif (lado1 == lado2 or lado2==lado3 or lado3==lado1):
    print("o triangulo é isoceles")
else:
    print("o triangulo é escaleno")