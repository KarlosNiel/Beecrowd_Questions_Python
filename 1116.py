N = int(input())

for e in range(N):
    X, Y = map(int, input().split())

    if Y == 0:
        print("divisao impossivel")

    else:
        print(f'{X / Y:.1f}')