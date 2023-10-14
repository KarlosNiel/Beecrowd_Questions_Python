def media(a, b, c, d):
    return (a*2 + b*3 + c*4 + d*1) / 10

N1, N2, N3, N4 = map(float, input().split())

print(f"Media: {media(N1, N2, N3, N4):.1f}")

if media(N1, N2, N3, N4) >= 7:
    print("Aluno aprovado.")

elif media(N1, N2, N3, N4) < 5:
    print("Aluno reprovado.")  

elif media(N1, N2, N3, N4) >= 5 and media(N1, N2, N3, N4) < 7:
    print("Aluno em exame.")

    NE = float(input())

    print(f"Nota do exame: {NE:.1f}")

    if (NE + media(N1, N2, N3, N4)) / 2 >= 5:
        print("Aluno aprovado.")

    elif (NE + media(N1, N2, N3, N4)) / 2 < 5:
        print("Aluno reprovado.")

    print(f"Media final: {(NE + media(N1, N2, N3, N4)) / 2:.1f}")




