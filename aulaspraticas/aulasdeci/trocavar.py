#Elabore um programa em Python que troque o valor de duas variáveis inteiras. Dica: Pense a solução que você usaria para trocar um líquido de um copo para outro.

var1 = int(5)
var2 = int(1)

print(f"variavel 1: {var1} e variavel 2: {var2}")

var3 = int(2)

var3 = var2
var2 = var1
var1 = var3


print(var1)
print(var2)