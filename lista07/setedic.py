while True:
    frase = input("Digite uma frase (-1 para sair): ")
    if frase == "-1":
        break
    
    dicionario = {}
    for char in frase:
        if char in dicionario:
            dicionario[char] += 1
        else:
            dicionario[char] = 1
    
    print("Dicionário ->", dicionario)