def distancia(a, a2, b, b2):
    return ((a2 - a) ** 2 + (b2 - b) ** 2) ** 0.5

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

print(f'{distancia(x1, x2, y1, y2):.4f}')