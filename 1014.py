def consumo(a, b):
    return a / b

distanciaP = int(input())
combustivelG = float(input())

print(f"{consumo(distanciaP, combustivelG):.3f} km/l")
