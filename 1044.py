def multiplos(a, b):
    if a % b == 0:
        return "Sao Multiplos"
    else:
        return "Nao sao Multiplos"



A, B = map(int, input().split())

print(multiplos(A, B))