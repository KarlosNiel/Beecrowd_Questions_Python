contador = 0
contador2 = 0

while contador < 6:
    x = float(input())
    if x > 0:
        contador2 += 1

    contador += 1

print(f"{contador2} valores positivos")
