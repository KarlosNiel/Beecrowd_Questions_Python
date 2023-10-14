def crescente(a, b, c):
    if a > b and b > c:
        maior = a
        meio = b
        menor = c
        
    elif a > c and c > b:
         maior = a
         meio = c
         menor = b
    
    elif b > a and a > c:
         maior = b
         meio = a
         menor = c
        
    elif b > c and c > a:
         maior = b
         meio = c
         menor = a
    
    elif c > a and a > b:
         maior = c
         meio = a
         menor = b
    
    elif c > b and b > a:
         maior = c
         meio = b
         menor = a

    return (f"{menor}\n{meio}\n{maior}")


x, y, z = map(int, input().split())

print(crescente(x, y, z))
print(f"\n{x}\n{y}\n{z}")
