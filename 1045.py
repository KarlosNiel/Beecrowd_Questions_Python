def nao_forma(a, b, c):
   return a >= b + c

def trian_retan(a, b, c):
   return a**2 == b**2 + c**2

def trian_obtuso(a, b, c):
   return a**2 > b**2 + c**2

def trian_acutan(a, b, c):
   return a**2 < b**2 + c**2

def trian_equila(a, b, c):
   return a == b == c

def trian_isos(a, b, c):
   return a == b != c or a == c != b or b == a != c or b == c != a or c == a != b or c == b != a

X, Y, Z = map(float, input().split())

if X > 0 and Y > 0 and Z > 0:
    if X >= Y and Y >= Z:
       A = X
       B = Y
       C = Z
        
    if X >= Z and Z >= Y: 
       A = X
       B = Z
       C = Y
        
    if Y >= X and X >= Z:
       A = Y
       B = X
       C = Z
            
    if Y >= Z and Z >= X:
       A = Y
       B = Z
       C = X

    if Z >= X and X >= Y:
       A = Z 
       B = X
       C = Y
        
    if Z >= Y and Y >= X:
       A = Z
       B = Y
       C = X
 

    if nao_forma(A, B, C):
      print("NAO FORMA TRIANGULO")
      
    else:
      if trian_retan(A, B, C):
         print("TRIANGULO RETANGULO")

      if trian_obtuso(A, B, C):
         print("TRIANGULO OBTUSANGULO")

      if trian_acutan(A, B, C):
         print("TRIANGULO ACUTANGULO")

      if trian_equila(A, B, C):
         print("TRIANGULO EQUILATERO")

      if trian_isos(A, B, C):
         print("TRIANGULO ISOSCELES")

