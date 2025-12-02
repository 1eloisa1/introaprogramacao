def maior(list):
    ma = 0
    for i in range(len(list)):
        if i == 0:
            ma = list[i]
        else:
            if list[i]>ma:
                ma = list[i]
    print(ma)

   
def main():
    lista = []
    continuar="s"
    while continuar in "sS":
        lista.append(int(input("numero: ")))
        continuar = input("continuar? ")
    maior(lista)
         
if(__name__ == "__main__"):
    main()
