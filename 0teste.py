def exponenciacao_recursiva(base, expoente):
    if expoente == 0:
        return 1
    elif expoente < 0:
        return 1 / exponenciacao_recursiva(base, -expoente)
    else:
        return base * exponenciacao_recursiva(base, expoente - 1)
    
print(exponenciacao_recursiva(2, 10))