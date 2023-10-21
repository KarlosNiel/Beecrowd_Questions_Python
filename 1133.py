X = int(input())
Y = int(input())

if X > 0 and Y > 0: 
    if X > Y:
        for e in range(Y + 1, X):
            if e % 5 == 2 or e % 5 == 3:
                print(e)

    if Y > X:
        for e in range(X + 1, Y):
            if e % 5 == 2 or e % 5 == 3:
                print(e)

        