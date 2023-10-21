def esfera(a):
    return (4 / 3)* 3.14159 * a ** 3

raio = float(input())

print(f"VOLUME = {esfera(raio):.3f}")