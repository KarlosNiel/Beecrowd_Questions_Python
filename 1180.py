n = int(input())
x = []
X = []

while len(x) < n:
    x[len(x):] = input().split()
    for e in x:
        e = int(e)
        X[len(X):] = [e]

menor = X[0]
posic = 0

for e in range(len(X)):
    if menor > X[e]:
        menor = X[e]
        posic = e

print(f"Menor valor: {menor}")
print(f"Posicao: {posic}")
        





