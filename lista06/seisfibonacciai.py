"""No século XIII, o matemático Leonardo Pisa, conhecido como Fibonacci, propôs a seguinte
sequência: (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...). Essa sequência tem uma lei de formação
simples; cada elemento, a partir do terceiro, é obtido somando-se os dois anteriores. Veja:
1+1=2, 2+1=3, 3+2=5 e assim por diante. Faça um programa que leia um número inteiro n
e exiba na tela a sequência de Fibonacci com n elementos. 
"""

n=int(input("Digite um Número: "))
fib=n
ultimo=1
penultimo=1
if n==1:
    print("1")
elif n==2:
    print("1 \n1")
else:
    print("1 \n1")
    for i in range(n-2):
        fib=ultimo+penultimo
        penultimo=ultimo
        ultimo=fib
        print(fib)