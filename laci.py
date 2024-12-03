import random

valasztas = "ox"

matrix = []

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

def OszlopEllenorzes():
    x_minta_1 = "xxxxx"
    kor_minta_1 = "ooooo"
    oszlop = ""

    szamlalo = 0


    for sor in matrix:
        oszlop += sor[j]

    print(oszlop)

            
        
        
    for _ in range(10):
        if x_minta_1 in oszlop:
            print(oszlop)
            print("Az X nyert")
            vege = True
        elif kor_minta_1 in oszlop:
            print(oszlop)
            print("A O nyert")
            vege = True

        

def SorEllenorzes():
    x_minta_1 = "xxxxx"
    kor_minta_1 = "ooooo"

    for sor in matrix:
        sor = "".join(sor)

        if x_minta_1 in sor:
            print(sor)
            print("Az X nyert(sor)")
            vege = True
        elif kor_minta_1 in sor:
            print(sor)
            print("A O nyert (sor)")
            vege = True

    


def Ellenorzes():
    SorEllenorzes()
    OszlopEllenorzes()

Megjelenit()

Ellenorzes()

