def maiorABC(a, b, c):
    maiorAB = (a + b + abs(a - b)) / 2
    return (maiorAB + c + abs(maiorAB - c)) / 2

A, B, C = map(int, input().split())

print(f"{maiorABC(A, B, C):.0f} eh o maior")