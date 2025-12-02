valordoproduto = float(input("O Valor do Produto: "))
formadepagamento = (input("Forma de Pagamento: (cheque, cartao ou dinheiro) "))

if (valordoproduto >= 100 and formadepagamento == "dinheiro"):
    valorfinal = (valordoproduto*0.90)
    print(f"R$ {valorfinal}")
elif (formadepagamento == "cheque"):
    valorfinal = valordoproduto
    print(f"R$ {valorfinal}")
elif (valordoproduto < 100 and formadepagamento == "dinheiro" or formadepagamento == "cheque"):
    valorfinal = valordoproduto
    print(f"R$ {valorfinal}")
elif (formadepagamento == "cartao"):
    tipocred = input("credito ou debito? ")
    if (tipocred == "credito"):
        parcelas = int(input("Digite o Número de Parcelas (1, 2 ou 3)"))
        if (parcelas == 1):
            valorfinal = valordoproduto
            print(f" R$ {valorfinal}")
        elif (parcelas == 2):
            valorfinal = valordoproduto/2
            print(f"R$ {valordoproduto} \n2 parcelas de R$ {valorfinal}")
        elif (parcelas == 3):
            valorfinal = valordoproduto/3
            print(f"R$ {valordoproduto} \n3 parcelas de R$ {valorfinal}")
        else:
            print("Quantidade de Parcelas Inválidas")
    elif (tipocred == "debito"):
        valorfinal = valordoproduto
        print(f"R$ {valorfinal}")
    else:
        print("Forma de pagameto invalida!")

else:
    (formadepagamento != "cheque" or formadepagamento != "dinheiro" or formadepagamento != "cartao" )
    print("Forma de pagameto invalida!")