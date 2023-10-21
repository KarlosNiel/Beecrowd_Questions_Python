x = int(input())
y = int(input())

soma = 0

if x < y:
    for e in range(y - 1, x, -1):
        if e % 2 != 0:
            soma += e

if y < x:
    for e in range(x - 1, y, -1):
        if e % 2 != 0:
            soma += e

print(soma)
