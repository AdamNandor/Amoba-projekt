import os

def Megjelenit():
    os.system('cls')
    szamlalo = 0
    print("     1   2   3   4   5   6   7   8   9   10".center(200))
    print("   ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐".center(200))
    for i in matrix:
        szamlalo += 1
        sor = " | ".join(i)
        
        if szamlalo != 10:
            print(f" {szamlalo} | {sor} |".center(200))
            print("   ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤".center(200))
        else:
            print(f"{szamlalo} | {sor} |".center(200))
            print("   └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘".center(200))


def Eldontes(ellenorizendo, vege):
    if x_minta in ellenorizendo:
        Megjelenit()
        print("Az x nyert")
        vege = True
    elif kor_minta in ellenorizendo:
        Megjelenit()
        print("Az x nyert")
        vege = True
    elif lepesek == 101 and not vege:
        Megjelenit()
        print("Döntetlen")
        vege = True

    if vege:
        return vege

def OszlopEllenorzes(vege):
    oszlop = ""

    for i in range(10):
        oszlop = ""
        for sor in matrix:
            oszlop += sor[i]
        vege = Eldontes(oszlop, vege)

    if vege:
        return vege



def SorEllenorzes(vege):
    for sor in matrix:
        sor = "".join(sor)
        
        vege = Eldontes(sor, vege)
    
    if vege:
        return vege

def AtloEllenorzesJobb(vege):
    for i in range(6):
        for j in reversed(range(4, 10)):
            atlo = ""
            for x in range(5):
                atlo += matrix[x+i][j-x]
            vege = Eldontes(atlo, vege)
    if vege:
        return vege

def AtloEllenorzesBal(vege):
    for i in range(6):
        for j in range(6):
            atlo = ""
            for x in range(5):
                atlo += matrix[x + i][x + j]
            vege = Eldontes(atlo, vege)

    return vege

def Ellenorzes(vege):
    vege = OszlopEllenorzes(vege)
    vege = SorEllenorzes(vege)
    vege = AtloEllenorzesJobb(vege)
    vege = AtloEllenorzesBal(vege)

    if vege:
        return vege


def KarakterRegisztralas(poz, karakter):
    matrix[int(poz[0])-1][int(poz[1])-1] = karakter


def MatrixEpites():
    matrix = []

    for _ in range(10):
        sor = []
        for _ in range(10):
            sor.append(" ")
        matrix.append(sor)

    return matrix

def InputErvenyessegEldontes(kor, poz, karakter, vege):
    if not 0 < int(poz[0]) <= 10 or not 0 < int(poz[1]) <= 10 :
        print("a koordináták megadásánál a minimum érték 1 a maximum 10")
    else:
        if matrix[int(poz[0])-1][int(poz[1])-1] == " ":
                kor ^= True
                KarakterRegisztralas(poz, karakter)
                Megjelenit()
                vege = Ellenorzes(vege)
        else:
            print("Csak szabad/üres rublikákra tehet")

    return kor, vege
    


matrix = MatrixEpites()
kor_minta = "ooooo"
x_minta = "xxxxx"
vege = False
kor = False


Megjelenit()

lepesek = 0

while not vege:
    if not kor and not vege:
        poz = input("Kérem adja meg az x pozícióját (sor, oszlop) --> ").split(", ")
        lepesek += 1
        kor, vege = InputErvenyessegEldontes(kor, poz, "x", vege)

    if kor and not vege:
        poz = input("Kérem adja meg az o pozícióját (sor, oszlop) --> ").split(", ")
        lepesek += 1

        kor, vege = InputErvenyessegEldontes(kor, poz, "o", vege)

        
input("Nyomjon entert a kilépéshez")
