#1 Escreva um programa que receba cinco valores do usuário e os armazene em uma lista.

lista=[]
for i in range(5):
    lista.append(int(input(f"numero {i+1}: ")))
   
print(lista)