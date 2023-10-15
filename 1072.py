N = int(input())
contador = 1
i = 0
o = 0 

while contador <= N:
    X = int(input())
    if X >= 10 and X <= 20:
        i += 1
    else:
        o += 1

    contador += 1

print(f"{i} in")
print(f"{o} out")