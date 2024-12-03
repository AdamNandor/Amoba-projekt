matrix = []

for i in range(10):
    sor = []
    for j in range(10):
        sor.append("")
    matrix.append(sor)

for i in matrix:
    for j in i:
        print(f"{i}")
