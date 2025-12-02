"""um desconto de 10% para os clientes que gastarem R$ 100 ou mais e pagarem em dinheiro. Escreva um programa que receba como entrada o 
valor do produto comprado e a forma de pagamento escolhida (dinheiro ou cheque), calcule o desconto devido (caso necessário)
 e exiba o valor final a ser pago.
"""

valordoproduto = float(input("O valor do Produto: "))
formadepagamento = (input("Forma de pagamento: (cheque ou dinheiro) "))


if (valordoproduto >= 100 and formadepagamento == "dinheiro"):
    valorfinal = (valordoproduto*0.90)
    print(f"R$ {valorfinal}")
elif (formadepagamento == "cheque"):
    valorfinal = valordoproduto
    print(f"R$ {valorfinal}")
elif (valordoproduto < 100 and formadepagamento == "dinheiro" or formadepagamento == "cheque"):
    valorfinal = valordoproduto
    print(f"R$ {valorfinal}")
else:
    (formadepagamento != "cheque" or formadepagamento != "dinheiro")
    print("Forma de pagameto invalida!")