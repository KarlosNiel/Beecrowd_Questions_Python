I = 1
J = 7

print(f"I={I} J={J}")

while True:
    J -= 1

    if J == 4:
        I += 2
        J = 7

    print(f"I={I} J={J}")

    if I == 9 and J == 5:
        break