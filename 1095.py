I = 1
J = 60

print(f"I={I} J={J}")

while True:
    I += 3
    J -= 5 
    
    print(f"I={I} J={J}")

    if J == 0:
        break