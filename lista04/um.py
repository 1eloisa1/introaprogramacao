#Escreva um programa que efetue a soma de todos os números ímpares que são múltiplos 
# de três e que se encontram no conjunto dos números de 1 até 500. 
nun1=0 
soma=0
while nun1<=499:
    nun1+=1
    if nun1%2!=0 and nun1%3==0:
        soma+=nun1
        print(soma)
            
print(f"total é {soma}")