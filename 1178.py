# Valor flutuante que será dividido no vetor:
x = float(input())

# Estrutura de repetição para dividir (x) o maximo possivel de acordo com o  que a questão pede:
while True:
    for i in range(100):
        # Imprimir o vetor:
        print(f"N[{i}] = {x:.4f}")
        # Variavel (x) que recebe o própio valor dividido por 2:
        x = x / 2
        
    # Condição para encerrar a repetição:
    if i == 99:
        break