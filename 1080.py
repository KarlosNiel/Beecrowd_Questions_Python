inicio = 1
maior = 0
posicao = 0

while inicio <= 100:
    entrada = int(input())

    if entrada > maior:
        maior = entrada
        posicao = inicio

    inicio += 1

print(maior)
print(posicao)