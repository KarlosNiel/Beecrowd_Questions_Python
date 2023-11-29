n = int(input())

for e in range(1, n + 1):
    num = e
    quadrado = e**2
    cubo = e**3
    print(f"{num} {quadrado} {cubo}")
    print(f"{num} {quadrado + 1} {cubo + 1}")