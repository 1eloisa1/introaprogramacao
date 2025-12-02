
"""Faça um programa que leia uma senha. Caso o usuário digite a senha errada, a mensagem
“Senha incorreta. Digite novamente” deve ser mostrada. Porém, se o usuário digitar a
senha errada 3 vezes, a seguinte mensagem deve ser mostrada: “Senha bloqueada.”
"""
senha="1234"
contador=1
senha1=input("Digite o sua senha:")
if(senha==senha1):
    print("Senha correta!")
else:
    while(input!=senha):
        senha1=input("senha incorreta. Digite novamente")
        contador=contador+1
        if(senha1==senha):
            print("Senha correta!")
            break
        if (contador==3):
            print("Senha bloqueada.")
            break