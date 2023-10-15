contador = 0
soma = 0
x = 1

while x <= 6:
    entrada = float(input())
    
    if entrada > 0:
        contador += 1
        soma += entrada
    x += 1

print(f"{contador} valores positivos")
print(f"{soma / contador:.1f}")