"""Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros
no período. """

depin=float(input("Digite o Depósito Inicial: "))
taxajuros=float(input("Digite a Taxa de Juros: "))
saldo=depin
for i in range(1, 25):
    juros=(saldo*(taxajuros/100))
    saldo+=juros
    print(f"Juros no mês {i} é {saldo:.2f} (Sob juros: {juros:.2f} reais)")
ganho_juros=saldo-depin
print(f"Ganho com juros: {ganho_juros:.2f}, Ganho total: {saldo:.2f}")

