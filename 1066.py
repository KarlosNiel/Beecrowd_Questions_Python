L = [-5, 0, -3, -4, 12]

par_c = 0
impar_c = 0 
posi_c = 0
nega_c = 0

for e in L:
    if e > 0:
        posi_c += 1

    if e < 0: 
        nega_c += 1

    if e % 2 == 0:
        par_c += 1

    if e % 2 != 0:
        impar_c += 1


print(f"{par_c} valor(es) par(es)")
print(f"{impar_c} valor(es) impar(es)")
print(f"{posi_c} valor(es) positivo(s)")
print(f"{nega_c} valor(es) negativo(s)")