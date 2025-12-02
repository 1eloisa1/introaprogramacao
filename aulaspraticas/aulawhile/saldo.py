"""Crie um programa para gerenciar uma conta bancária, apresentando o seguinte menu para
o usuário:
<1> Depositar
<2> Sacar
<3> Consultar saldo
<4> Sair
Digite o valor da opção:
O menu deve ser exibido repetidamente até que o usuário digite 4, que é o valor da opção
para sair do programa. Caso o usuário tente sacar um valor maior do que o saldo atual da
conta, uma mensagem deve informá-lo que ele não possui saldo suficiente para a
operação. """
saldo=10000
print("<1> Depositar \n<2> Sacar \n<3> Consultar saldo \n<4> Sair")
menu=input("Digite o valor da opção:")
while (menu!="4"):
    if(menu=="1"):
        deposito=float(input("Quanto quer depositar?"))
        saldo=saldo+deposito
        menu=input("Digite o valor da opção:")
        continue
    elif (menu=="2"):
        saque=float(input("Quanto deseja sacar?"))
        if(saque>saldo):
            print("Você não possui saldo suficiete")
        else:
            saldo=saldo-saque
        menu=input("Digite o valor da opção:")
        continue
    elif (menu=="3"):
        print(f"Seu saldo é {saldo}")
        menu=input("Digite o valor da opção:")
        continue