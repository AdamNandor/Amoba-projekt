
matrix = []
matrix2 = []
print("   1   2   3   4   5   6   7   8   9   10")
for i in range(10):
    sor = []
    for j in range(10):
        sor.append("")
    matrix2.append(sor)

    szamlalo = 0

for i in matrix2:
    szamlalo += 1
    sor = " | ".join(i)
    print(f"{szamlalo}  | {sor} |")