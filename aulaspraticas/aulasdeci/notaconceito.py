"""Escreva um programa que receba as 3 notas obtidas por um aluno, calcule a média
aritmética de aproveitamento e apresente o conceito e a situação do aluno (APROVADO
ou REPROVADO). O aluno é considerado APROVADO se tiver conceito A, B ou C e
REPROVADO, caso obtenha conceitos D e E. A atribuição de conceitos obedece à tabela
abaixo:
Conceito Média de aproveitamento
A A partir de 9,0
B De 7,5 a 9,0
C De 6,0 a 7,5
D De 4,0 a 6,0
E Abaixo de 4,0"""
nota1=float(input("Digite sua 1° nota:"))
nota2=float(input("Digite sua 2° nota:"))
nota3=float(input("Digite sua 3° nota:"))

media = (nota1+nota2+nota3)/3
if (media>6):
    print("Aprovado")
    if (media>=6):
        print("seu conceito é c")
    elif (media>=7,5):
        print("seu conceito é b")
    else:
        (media>=9)
        print("seu conceito é a")
else:
    print("reprovado")
    if(media>=4):
        print("seu conceito é d")
    else:
        print("seu conceito é e")