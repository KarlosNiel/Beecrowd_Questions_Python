N = int(input())
coelhos = 0
ratos = 0
sapos = 0

for e in range(N):
    quant, tipo = input().split()
    quant = int(quant)
    tipo = str(tipo)

    if quant >= 1 and quant <= 15:
        if tipo == "C":
            coelhos += quant

        elif tipo == "R":
            ratos += quant

        elif tipo == "S":
            sapos += quant

cobaias = coelhos + ratos + sapos

print(f"Total: {cobaias} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {(coelhos / cobaias)*100:.2f} %")
print(f"Percentual de ratos: {(ratos / cobaias)*100:.2f} %")
print(f"Percentual de sapos: {(sapos / cobaias)*100:.2f} %")
