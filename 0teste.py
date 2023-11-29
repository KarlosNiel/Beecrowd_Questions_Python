# def exponenciacao_recursiva(base, expoente):
#     if expoente == 0:
#         return 1
#     elif expoente < 0:
#         return 1 / exponenciacao_recursiva(base, -expoente)
#     else:
#         return base * exponenciacao_recursiva(base, expoente - 1)
    
# print(exponenciacao_recursiva(2, 10))

# my_list = [1, 2, 3, 4, 5]
# last_index = len(my_list) - 1  # O último índice é o comprimento da lista menos 1

# for i in range(len(my_list)):
#     if i == last_index:
#         print("Este é o último item:", my_list[i])

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# linha = int(input())

# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))



# if linha > 0:
#     for l in range(linha, linha + 1):
#         for c in range(0, 3):
#             print(f"[{matriz[l][c]:^5}]", end="")
#         print()
    
# elif linha == 0:
#     for l in range(linha, 1):
#         for c in range(0, 3):
#             print(f"[{matriz[l][c]:^5}]", end="")
#         print()

# matriz = [[0, 0, 0], 
#           [0, 0, 0],
#           [0, 0, 0]]

# linha = int(input())
# oper = str(input())
# soma = 0

# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c]= float(input(f"Digite um valor para [{l}, {c}]: "))



# if linha > 0:
#     for l in range(linha, linha + 1):
#         for c in range(0, 3):
#             soma += matriz[l][c]
#             print(f"[{matriz[l][c]:^5}]", end="")

    
# elif linha == 0:
#     for l in range(linha, 1):
#         for c in range(0, 3):
#             soma += matriz[l][c]
#             print(f"[{matriz[l][c]:^5}]", end="")

# if oper == "S":
#     print(f"{soma:.1f}")

# if oper == "M":
#     print(f"{soma / 3:.1f}")

operation = input()

matrix = []

for i in range(12):
    row = []
    for j in range(12):
        row[j:j] = [float(input())]
    matrix += [row]

result = 0
count = 0

for i in range(12):
    for j in range(12):
        if j > i:
            result += matrix[i][j]
            count += 1

if operation == 'M':
    result /= count

print(f'{result:.1f}')