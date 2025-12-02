"""Crie um programa que tenha como entrada a altura (h) de uma pessoa, calcule e exiba seu
peso ideal, utilizando as seguintes fórmulas:
• Para homens: (72.7*h) - 58
• Para mulheres: (62.1*h) - 44.7"""
h = float(input('Digite a altura:'))
peso_ideal_homem = (72.7*h)-58
peso_ideal_mulher = (62.1*h)-44.7
print(f'O peso ideal para homens é: {peso_ideal_homem} e o peso ideal para mulheres é: {peso_ideal_mulher}')