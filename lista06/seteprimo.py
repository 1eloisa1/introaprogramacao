"""7) Escreva um programa que leia um número e verifique se ele é primo. Para fazer essa
verificação, calcule o resto da divisão do número informado por todos os número menores
que ele a partir de 2. Se o resto de uma dessas divisões for igual a 0, o número não é
primo. Note que 0 e 1 não são primos e que 2 é o único primo que é par. 
"""

n=int(input("Digite um Número: "))
if n==2:
    print(f" {n} é primo")
elif n==0 or n==1:
    print(f"{n} não é primo")
else:
    for i in range(2,n):
        if n%i==0:
            print(f"{n} não é primo")
            break
        elif n%i!=0 and i==n-1:
            print(f"{n} é primo")
