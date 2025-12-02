import numpy as np

def mdf(list):
    soma = 0
    for i in range(len(list)):
        soma+=list[i]
    media = soma/len(list)
    desvio_padrao = np.std(list)
    print(f"desvio padrao {desvio_padrao} e media {media}")

def main():
    n = int(input('tamanho da lista:'))
    lista=[]
    for i in range(n):
        lista.append(int(input("valor na lista: ")))
    mdf(lista)

if(__name__ == "__main__"):
    main()