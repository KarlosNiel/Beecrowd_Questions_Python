# Valor inteiro (2 <= t <= 50):
t = int(input())

# Sequencia de valores de 0 ate t-1 em 1000 listas:
n = [0] * 1000

# Módulo dos numéros cujo irão se repetir, por exemplo se t = 3, será: 0 % 3 == 0, 1 % 3 == 1, 2 % 3 == 2, 3 % 3 == 0, 4 % 3 == 1...:
for i in range(1000):
    n[i] = i % t

# Imprimir o vetor e os valores armazenados:
for i in range(1000):
    print(f"N[{i}] = {n[i]}")