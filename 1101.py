M, N = map(int, input().split())

soma = 0

if M > 0 and N > 0:
    if M > N:
        cont = N - 1

        while True:
            cont += 1
            soma += cont
            print(f"{cont}", end=" ")

            if cont == M:
                break

            

    elif N > M:
        cont = M - 1

        while True:
            cont += 1
            soma += cont
            print(f"{cont}", end=" ")

            if cont == N:
                break

    print(f"Sum={soma}")