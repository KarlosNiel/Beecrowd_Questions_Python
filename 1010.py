def v_pagar(a, b, c, d):
    return a*b + c*d

cod, quant, val = input().split()
cod = int(cod)
quant = int(quant)
val = float(val)

cod2, quant2, val2 = input().split()
cod2 = int(cod2)
quant2 = int(quant2)
val2 = float(val2)

print(f"VALOR A PAGAR: R$ {v_pagar(quant, val, quant2, val2):.2f}")
