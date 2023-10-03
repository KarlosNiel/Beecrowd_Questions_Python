def salario_t(a, b):
    return a + (b * 0.15)

nome = input()
salario_f = float(input())
vendas = float(input())

print(f"TOTAL = R$ {salario_t(salario_f, vendas):.2f}")