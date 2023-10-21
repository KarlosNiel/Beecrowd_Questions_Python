cont = 0
soma = 0

while True:
    N = float(input())

    if N >= 0 and N <= 10:
        cont += 1
        soma += N 
    
        if cont == 2:
            print(f"media = {soma / cont}")

    else:
        print("nota invalida")



