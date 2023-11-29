matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

L = int(input())
oper = str(input())
soma = 0

for linha in range(0, 12):
    for coluna in range(0, 12):
        matriz[linha][coluna] = float(input())

if L > 0:
    for linha in range(L, L + 1):
        for coluna in range(0, 12):
            soma += matriz[linha][coluna]
    
elif L == 0:
    for linha in range(L, 1):
        for coluna in range(0, 12):
            soma += matriz[linha][coluna]

if oper == "S":
    print(f"{soma:.1f}")

if oper == "M":
    print(f"{soma / 12:.1f}")