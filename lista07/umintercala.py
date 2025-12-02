elemento = 5
v1 = []
v2 = []
v3 = []

for i in range (elemento):
    v1.append( int (input("Elemento do vetor 1: ") ) )

for i in range (elemento):
    v2.append( int (input("Elemento do vetor 2: ") ) )

for i in range(elemento):
    v3.append(v1[i])
    v3.append(v2[i])

print("O vetor com os elementos intercalados dos vetores 1 e 2 é: ")
for i in range(elemento * 2):
    print(v3[i], end=" ")