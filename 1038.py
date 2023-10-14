def menu(x, y):
    if x == 1:
      return y * 4 
   
    elif x == 2:
     return y * 4.5
   
    elif x == 3:
      return y * 5
   
    elif x == 4:
      return y * 2

    elif x == 5:
      return y * 1.5


cod, quant = map(int, input().split())

print(f"Total: R$ {menu(cod, quant):.2f}")

