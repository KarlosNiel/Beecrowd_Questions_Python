N = int(input())

contador = 0 
Xc = 0
Yc = 0

while contador < N:
    X, Y = map(int, input().split())

    if X == Y: 
        print("0")

    elif X < Y:
        while X < Y:
            if X % 2 != 0:
                Xc += X
                print(Xc)
            X += 1

    elif Y < X:
        while Y < X:
            if Y % 2 != 0:
                Yc += Y
                print(Yc)
            Y += 1

    Xc = 0
    Yc = 0
        
    contador += 1



