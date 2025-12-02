'''Escreva um programa que leia idades de uma turma de alunos e calcule a maior e a menor
idades informadas. O número de alunos da turma deve ser informado pelo usuário. Dica:
Você deve usar variáveis auxiliares (maior e menor) para manter a maior e a menor nota
digitadas pelo usuário. No caso da maior nota, você deve verificar, a cada iteração, se a
nota atual digitada pelo usuário é maior que a variável maior. Em caso positivo, você
dever atribuir tal valor à variável maior. Para a menor nota, o raciocínio é similar.'''
nunalunos=int(input("qual o numero de alunos? "))
nota=int(input("digite nota: "))
menor=maior=nota
for i in range(0, nunalunos-1):
    nota=int(input("digite nota: "))
    if (nota<menor):
        menor=nota
    if(nota>maior):
        maior=nota
print(f"a maoir é {maior} e a menor é {menor}")