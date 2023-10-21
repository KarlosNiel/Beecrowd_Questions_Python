def aumento15(a):
    return a*0.15
    
def aumento12(a):
    return a*0.12
    
def aumento10(a):
    return a*0.10
    
def aumento07(a):
    return a*0.07
    
def aumento04(a):
    return a*0.04
    
x = float(input())

if x >= 0 and x <= 400:
    print(f"Novo salario: {x + aumento15(x):.2f}") 
    print(f"Reajuste ganho: {aumento15(x)}")
    print("Em percentual: 15%")

elif x > 400 and x <= 800:
    print(f"Novo salario: {x + aumento12(x):.2f}") 
    print(f"Reajuste ganho: {aumento12(x)}")
    print("Em percentual: 12%")

elif  x > 800 and x <= 1200:
    print(f"Novo salario: {x + aumento10(x):.2f}")
    print(f"Reajuste ganho: {aumento10(x)}")
    print("Em percentual: 10%")

elif x > 1200 and x <= 2000:
    print(f"Novo salario: {x + aumento07(x):.2f}") 
    print(f"Reajuste ganho: {aumento07(x)}")
    print("Em percentual: 7%")

elif x > 2000:
    print(f"Novo salario: {x + aumento04(x):.2f}") 
    print(f"Reajuste ganho: {aumento04(x)}")
    print("Em percentual: 4%")