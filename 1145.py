x, y = map(int, input().split())

cont_inicial = 1
cont_atual = x

while True:
    for e in range(cont_inicial, cont_atual):
        print(f"{e}", end=" ")
        if e == cont_atual - 1:
            print("")
        

    cont_inicial += x
    cont_atual += x 
    
    if cont_inicial >= y:
        break
    




