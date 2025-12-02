m = [ [None] * 3 for i in range(3)]
for i in range(3):
    for j in range(3):
        m[i][j] = int( input( f"ELEMENTO [{i+1} e {j+1}]: ") )

print("original: ")
for i in range (3):
    print(f"{m[i]}")


mc = [linha[:] for linha in m]
for i in range (3):
    m[1][i] = mc[i][1]
    m[i][1] = mc[1][i]


print("modificada: ")
for i in range (3):
    print(f"{m[i]}")

