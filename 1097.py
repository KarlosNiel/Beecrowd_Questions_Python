I = 1
J = 7
contador = 0 

print(f"I={I} J={J}")

while True:
    J -= 1
    contador += 1

    if contador == 3:
        I += 2
        J += 5
        contador = 0

    print(f"I={I} J={J}")

    if I == 9 and J == 13:
        break