import random

vege = False

matrix = []

for i in range(10):
    sor = []
    for j in range(10):
        sor.append(" ")
    matrix.append(sor)
print("     1   2   3   4   5   6   7   8   9   10")
def Megjelenit():
    szamlalo = 0
    print("   ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐")
    for i in matrix:
        szamlalo += 1
        sor = " | ".join(i)
        
        if szamlalo != 10:
            print(f"{szamlalo}  | {sor} |")
            print("   ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
        else:
            print(f"{szamlalo} | {sor} |")
            print("   └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘")

def OszlopEllenorzes(vege):
    x_minta_1 = "xxxxx"
    kor_minta_1 = "ooooo"
    oszlop = ""

    for i in range(10):
        oszlop = ""
        for sor in matrix:
            oszlop += sor[i]
            
        if x_minta_1 in oszlop:
            print(oszlop)
            print("Az x nyert")
            vege = True
            print(vege, "oszlop")
        elif kor_minta_1 in oszlop:
            print("A o nyert")
            vege = True

    if vege:
        return vege



def SorEllenorzes(vege):
    x_minta_1 = "xxxxx"
    kor_minta_1 = "ooooo"

    for sor in matrix:
        sor = "".join(sor)

        if x_minta_1 in sor:
            print("Az x nyert(sor)")
            vege = True
            print(vege, "sor")
        elif kor_minta_1 in sor:
            print("A o nyert (sor)")
            vege = True
    
    if vege:
        return vege
    

def AtloEllenorzes(vege):
    if vege:
        return vege
    

def Ellenorzes(vege):
    vege = OszlopEllenorzes(vege)
    vege = SorEllenorzes(vege)
    vege = AtloEllenorzes(vege)

    if vege:
        return vege


def KarakterRegisztralas(poz, karakter):
    matrix[int(poz[0])-1][int(poz[1])-1] = karakter

kor = False

Megjelenit()

while not vege:
    if not kor:
        poz = input("Kérem adja meg az x pozícióját (sor, oszlop) --> ").split(", ")
        kor = True
        karakter = "x"
    elif kor:
        poz = input("Kérem adja meg az o pozícióját (sor, oszlop) --> ").split(", ")
        kor = False
        karakter = "o"

    
    KarakterRegisztralas(poz, karakter)
    Megjelenit()
    vege = Ellenorzes(vege)
