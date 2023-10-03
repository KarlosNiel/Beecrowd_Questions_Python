def sal(a, b):
    return a * b

num_f = int(input())
horas_t = int(input())
salario_h = float(input())

print(f'NUMBER = {num_f}')
print(f'SALARIO = U$ {sal(horas_t, salario_h):.2f}')
