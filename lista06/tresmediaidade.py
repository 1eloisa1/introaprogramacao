"""Faça um programa que peça para 𝑛 pessoas a sua idade, ao final o programa deverá
verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então,
dizer se a turma é jovem, adulta ou idosa, conforme a média calculada. 
"""
pessoas=int(input("Quantas Pessoas tem a Turma? "))
soma=0
for i in range(pessoas):
    idade=int(input("Digite a Idade: "))
    soma+=idade
media=soma/pessoas
if media<=25:
    print("Turma é Jovem")
elif media<=60:
    print("Turma é Adulta")
else:
    print("Turma é Idosa")

print(f"A Média da Idade é: {media:.2f}")


