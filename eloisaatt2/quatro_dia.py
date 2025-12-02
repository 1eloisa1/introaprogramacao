"""Faça um programa que solicite ao usuário o turno que ele estuda, a partir dos caracteres a seguir: M (matutino), V (vespertino) ou N (noturno).
Depois disso, o programa deve exibir as mensagens "Bom Dia!", "Boa Tarde!", "Boa Noite!" ou "Valor Inválido!", conforme cada caso."""""

turno = input("Qual turno que você estuda: matutino digite m, vespertino digite t ou noturno digite n? ")

if (turno == "m"):
    print("Bom Dia!")
elif (turno == "v"):
    print("Boa Tarde!")
elif (turno == "n"):
    print("Boa Noite!")
else:
    print("Valor invalido!")