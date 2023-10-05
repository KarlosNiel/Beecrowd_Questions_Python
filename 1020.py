total = int(input())

anos = total // 365
meses = (total % 365) // 30
dias = (total % 365) % 30

print(f"{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)")