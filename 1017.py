def litros_G(a, b):
    return (a / 12) * b

tempos_G = int(input())
velo_Media = int(input())

print(f"{litros_G(tempos_G, velo_Media):.3f}")