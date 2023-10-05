N = int(input())

segundos = N % 60
minutos = (N % 3600) // 60
horas = N // 3600

print(f"{horas}:{minutos}:{segundos}")