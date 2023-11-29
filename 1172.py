X = []

while len(X) < 10:
    x = int(input())
    X[len(X):] = [x]

for i in range(len(X)):
    if X[i] <= 0:
        X[i] = 1

    print(f"X[{i}] = {X[i]} ")