def trian(a, c):
    return a * c / 2

def circ(c):
    return 3.14159 * c ** 2

def trape(a, b, c):
    return (a + b)*c / 2

def quad(b):
    return b ** 2

def retan(a, b):
    return a*b

a, b, c = map(float, input().split())

print(f"TRIANGULO: {trian(a, c):.3f}")
print(f"CIRCULO: {circ(c):.3f}")
print(f"TRAPEZIO: {trape(a, b, c):.3f}")
print(f"QUADRADO: {quad(b):.3f}")
print(f"RETANGULO: {retan(a, b):.3f}")