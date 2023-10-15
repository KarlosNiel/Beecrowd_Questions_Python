def imposto(a):
    if a >= 0 and a <= 2000:
        print("Isento")

    elif a > 2000 and a <= 3000:
        print(f"R$ {(a - 2000)*0.08:.2f}")

    elif a > 3000 and a <= 4500:
        print(f"R$ {(a - 3000)*0.18 + 80:.2f}")
    
    elif a > 4500:
        print(f"R$ {(a - 4500)*0.28 + 350:.2f}")

renda = float(input())

imposto(renda)