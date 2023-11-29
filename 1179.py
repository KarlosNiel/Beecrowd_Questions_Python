impar = []
par = []
cont = 0

while True:
    x = int(input())

    if x % 2 == 0:
        par[len(par):] = [x]
        if len(par) == 5:
            for i in range(len(par)):
                print(f"par[{i}] = {par[i]}")
            par = []

    if x % 2 != 0:
        impar[len(impar):] = [x]
        if len(impar) == 5:
            for i in range(len(impar)):
                print(f"impar[{i}] = {impar[i]}")
            impar = []
    
    cont += 1
    if cont == 15:
       break

for i in range(len(impar)):
    print(f"impar[{i}] = {impar[i]}")

for i in range(len(par)):
    print(f"par[{i}] = {par[i]}")


    

