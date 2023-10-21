N = int(input())

for e in range(N):
    n = int(input())

    if n % 2 == 0 and n > 0:
        print("EVEN POSITIVE")
    
    if n % 2 == 0 and n < 0:
        print("EVEN NEGATIVE")

    if n % 2 != 0 and n > 0:
        print("ODD POSITIVE")

    if n % 2 != 0 and n < 0:
        print("ODD NEGATIVE")

    if n == 0:
        print("NULL")