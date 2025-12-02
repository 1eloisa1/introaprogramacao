"""Implemente um programa que pergunte o valor inicial de uma dívida e o juro mensal.
Pergunte também o valor mensal que será pago. Exiba na tela o número de meses em que
a dívida será paga, o total pago e o total de juros pago. 
"""

valorin=float(input("Qual o valor inicial da divida? "))
jurosmes=float(input("Qual o valor de juros por mês? "))
pagomes=float(input("Valor pago por mês? "))
mes=1
if valorin*(jurosmes/100)<pagomes:
    valorpago=0
    saldo=valorin
    while saldo>pagomes:
        juros=saldo*(jurosmes/100)
        saldo+=juros-pagomes
        valorpago+=juros
        print(f"no mes {mes}, a divida é: {saldo:6.2f}")
        mes+=1
    print(f"para pagar {valorin:6.2f} pagara uma taxa de {jurosmes:6.2f}")
    print(f"pagará {mes-1} meses de {valorpago:6.2f}")
else:
    print("A divida nao sera paga, pois os juros sao maiores que o pagamento mensal.")