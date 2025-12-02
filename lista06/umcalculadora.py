""") Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro
entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída
deve ser conforme o exemplo abaixo. Tabuada de 5:
5 X 1 = 5 
"""
nun=int(input("Digite um Número: "))
print(f"Tabuada de {nun}: ")
for i in range(1, 11):
    nume=nun*i
    print(f"{nun} x {i} = {nume}")

