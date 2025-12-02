"""Implemente um programa que pergunte quanto um trabalhador ganha por hora e o
número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido
mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
para o sindicato. O programa deve exibir as seguintes informações:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido."""


salario_hora = float(input('Digite o seu salario por hora:'))
horas_trabalhadas = float(input('Digite o numero de horas trabalhadas:'))

salario_bruto = (salario_hora*horas_trabalhadas)
salario_inss = (salario_bruto)*(8/salario_bruto)
salario_sindicato = (salario_bruto)*(5/salario_bruto)
salario_imposto_renda = (salario_bruto)*(11/salario_bruto)
salario_liquido = (salario_bruto)-(salario_sindicato)-(salario_inss)-(salario_imposto_renda)

print(f"Salário Bruto: R$ {salario_bruto}")
print(f"IR(11%): R$ {salario_imposto_renda}")
print(f"INSS(8%): R$ {salario_inss}")
print(f"Sindicato(5%): R$ {salario_sindicato}")
print(f"O salario liquido: R$ {salario_liquido}")
