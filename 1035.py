def selecao(a, b, c, d):
    if b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0:
        return("Valores aceitos")
    else:
        return("Valores nao aceitos")
   

A, B, C, D = map(int, input().split())

print(selecao(A, B, C, D))