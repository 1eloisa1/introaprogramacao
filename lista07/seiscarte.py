N = int(input("Digite o número de pontos: "))

pontos = []
for i in range(N):
    x = float(input(f"Digite x{i+1}: "))
    y = float(input(f"Digite y{i+1}: "))
    pontos.append((x, y))

distancias = []
for i in range(N):
    for j in range(i + 1, N):
        d = ((pontos[i][0] - pontos[j][0])**2 + (pontos[i][1] - pontos[j][1])**2) ** 0.5
        distancias.append(d)

distancia_minima = distancias[0]
distancia_maxima = distancias[0]
total_distancias = 0

for d in distancias:
    if d < distancia_minima:
        distancia_minima = d
    if d > distancia_maxima:
        distancia_maxima = d
    total_distancias += d

distancia_media = total_distancias / len(distancias)

print(f"Distância mínima: {distancia_minima:.2f}")
print(f"Distância máxima: {distancia_maxima:.2f}")
print(f"Distância média: {distancia_media:.2f}")