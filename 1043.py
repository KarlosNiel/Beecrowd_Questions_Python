def perimetro(a, b, c):
    return (f"Perimetro = {a + b + c:.1f}")

def area_trapezio(a, b, c):
    return (f"Area = {(a + b)*c / 2:.1f}")

A, B, C = map(float, input().split())

if A + B > C and A + C > B and B + C > A:
    print(perimetro(A, B, C))

else:
    print(area_trapezio(A, B, C))

    
