"""Escreva um programa que calcule a raiz quadrada de um número. Utilize o método de
Newton para obter um resultado aproximado. Sendo 𝑛 o número a obter a raiz quadrada,
considere o valor inicial para a base 𝑏 = 2 e calcule 𝑝 usando a fórmula 𝑝 = (𝑏 +௡௕)/2. A
cada passo, faça 𝑏 = 𝑝 e recalcule 𝑝 usando a fórmula apresentada. Pare quando a
diferença absoluta entre 𝑏 e 𝑝 for menor que 0,0001. Os valores de 𝑏 e 𝑝 representam o
valor da raiz quadrada do número informado. Exiba-os na tela. Dica: A função abs()
calcula o valor absoluto de um número passado por parâmetro. Ex.: abs(-10) resulta
em 10. 
"""
n=float(input("digite um numero: "))
b=2
p=0
while abs(n-(b*b))>0.0001:
    p=(b+(n/b))/2
    b=p
print(f"a raiz do número digitado é aproximadamente {p:3.2f}")
