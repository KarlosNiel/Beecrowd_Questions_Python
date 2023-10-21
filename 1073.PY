N = int(input())

if N > 5: 
    for e in range(1, N + 1):
        if e % 2 == 0:
            print(f"{e}^2 = {e**2}")