x = int(input())
contador = 0

while True:
    if x % 2 != 0:
        contador += 1
        print(x)
    x += 1

    if contador == 6:
        break

