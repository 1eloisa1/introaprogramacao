"""Elabore um programa que exiba os números de 50 a 10 e a soma dos valores nesse
intervalo. """

contador=50
soma=0
print(contador)
while (contador>=10):
    soma=contador+soma
    contador=contador-1
    if (contador !=9):
        print(contador)

print(soma)