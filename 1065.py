L = [7, -5, 6, -4, 12]

cont = 0 

for e in L:
    if e % 2 == 0:
        cont += 1
    
print(f"{cont} valores pares")