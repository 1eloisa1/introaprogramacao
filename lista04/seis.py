"""Desenvolva um programa para simular um simples sistema de vendas. Você deve solicitar
ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de
códigos abaixo a seguir para obter o preço da cada produto. 1 5,50
2 2,30
3 4,75
4 6,80
5 9,30 """


codigo=int(input("codigo: "))
total=0
while codigo!=0: 
    qtd=int(input("quantidade: "))
    if codigo==1:
        preco=5.50
        total+=preco*qtd
    elif codigo==2:
        preco=2.30
        total+=preco*qtd
    elif codigo==3:
        preco=4.75
        total+=preco*qtd
    elif codigo==4:
        preco=6.80
        total+=preco*qtd
    elif codigo==5:
        preco=9.30
        total+=preco*qtd
    else:
        print("codigo invalido, inicie novamente")
        codigo=int(input("codigo: "))
        continue
    codigo=int(input("codigo: "))
print(total)
