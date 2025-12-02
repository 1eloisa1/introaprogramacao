def dobro(a):
    dobr=a**2
    print(dobr)

   
def main():
    n = (int(input("numero: ")))
    dobro(n)
         
if(__name__ == "__main__"):
    main()


    """Faça um programa que solicite a data de nascimento (dd/mm/aaaa) e
imprima com o nome do mês por extenso.
Ex.:
Informe uma data: 25/10/2018
Data por extenso: 25 de outubro de 2018."""
data = input("data de aniversario: dd/mm/aa")
datana = data.split("/")
if datana[1] == 01:
    print(f"{datana[0]} de janeiro de {datana[2]}")
elif datana[1] == 02:
    print(f"{datana[0]} de fevereiro de {datana[2]}"
elif datana[1] == 03:
    print(f"{datana[0]} de março de {datana[2]}")
elif datana[1] == 04:
    print(f"{datana[0]} de abril de {datana[2]}")
elif datana[1] == 05:
    print(f"{datana[0]} de maio de {datana[2]}")
elif datana[1] == 06:
    print(f"{datana[0]} de junho de {datana[2]}")
elif datana[1] == 07:
    print(f"{datana[0]} de julho de {datana[2]}")
elif datana[1] == 08:
    print(f"{datana[0]} de agosto de {datana[2]}")
elif datana[1] == 09:
    print(f"{datana[0]} de setembro de {datana[2]}")
elif datana[1] == 10:
    print(f"{datana[0]} de outubro de {datana[2]}")
elif datana[1] == 11:
    print(f"{datana[0]} de novembro de {datana[2]}")
elif datana[1] == 12:
    print(f"{datana[0]} de dezembro de {datana[2]}")
else:
    print('valor invalido')