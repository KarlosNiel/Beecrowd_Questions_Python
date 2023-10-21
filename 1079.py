N = int(input())

if N > 0:
    for e in range(N):
        x, y, z = map(float, input().split())
        
        media = (x*2 + y*3 + z*5) / 10

        print(f"{media:.1f}")

