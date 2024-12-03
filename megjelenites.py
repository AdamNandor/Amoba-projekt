
for i in range(10):
    sor = []
    for j in range(10):
        sor.append(random.choice(valasztas))
    matrix.append(sor)



vege = False

def Megjelenit():
    szamlalo = 0

    for i in matrix:
        szamlalo += 1
        sor = " | ".join(i)
        print(f"{szamlalo} | {sor} |")
    
