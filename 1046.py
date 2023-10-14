x, y = map(int, input().split())

if x >= 0 and x <= 24 and y >= 0 and y <= 24:
    if x == y: 
        print("O JOGO DUROU 24 HORA(S)")

    elif x > y:
        N = (y + 24) - x
        print(f"O JOGO DUROU {N} HORA(S)")

    elif x < y: 
        M = y - x
        print(f"O JOGO DUROU {M} HORA(S)")


