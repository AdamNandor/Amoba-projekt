# Amőba-projekt

# Játéktér mejelenítés, Megjelenítés eljárás
A kereteket a rublikák között ┌ ─ ┬ ┐ ├ ─ ┼ ┤ └ ─ ┴ ┘ | karakterekkel rajzoltuk meg, a képen látható módon. A függvény továbbá letiszítja a képernyőről az eddigi információkat, így csak a pálya, az input mező és a játékhoz szükséges információk láthatóak

![kép](https://github.com/user-attachments/assets/62486f2e-67c0-4340-846e-c58f1138f82d)

# Ellenőrzés Függvény
Az ellenőrzés függvény az oszlopok átlók és sorok ellenőrzéség hívja meg egyszerre így csak ezt az egy függvény kell megvívni ha le akarjuk ellenőrizni a játékteret. Ennek a függvények az ellenőrizendő stringet és a vege booleant kell megadni paraméternek

![kép](https://github.com/user-attachments/assets/86dc812f-8da5-4744-b40d-3a1474368440)


# Eldöntés Függvény
ellenőrzi az egyesített oszlop, sor vagy átlóban szerepel-e egymás mellett 5 darab x vagy o és ha igen akkor a játékot leállítja. Ennek a függvénynek a vége booleant kell megadni paraméternek

![kép](https://github.com/user-attachments/assets/0d583e93-e782-4f4d-929b-26461b4c3313)

# Oszlopok Ellenőrzése
A sorokat az ellenőrzéshez egy string-é alakítjuk át ezután meghívjuk az Eldöntés() függvényt aminek megadjuk a stringet és ellenőrzi a fentebb leírtak szerint. A vege boolent kell megadni paraméternek

![kép](https://github.com/user-attachments/assets/1a9cd239-45f3-4d12-87a7-6224b6288a1e)

# Sorok Ellenőrzése
Az oszlopokhoz hasonlóan a sorokat is átalakítjuk egy string-é majd megvizsgáljuk az Eldöntés() függvénnyel. függvényparaméternek a vege boolent kell megadni

![kép](https://github.com/user-attachments/assets/f61a70ac-d71e-410e-aea2-811880bee63c)

# Átló Ellenőrzés
a sorokhoz és oszlopokhoz hasonlóan az átlókat is átalakítjuk string-é ezután megvizsgáljuk az Eldöntés() függvénnyel. A jobbra és balra dőlő átlókat külön vizsgáljuk. Itt is a vege boolent kell megadni paraméternek

![kép](https://github.com/user-attachments/assets/f1e4e3ed-8819-4f2d-be4d-ae6f9a7bcda6)
![kép](https://github.com/user-attachments/assets/dc3a6fe7-435c-4e2a-aec5-8074d4203d85)


# Karakter Regisztrálás 
A karakterek regisztrálása vagyis a mátrixba helyezése a megfelelő pozícióra. Ennek a függvények regisztrálás pozícióját, és a regisztrálni kívánt karaktert kell megadni

![kép](https://github.com/user-attachments/assets/8d8d6918-2329-4c6d-8621-6670c1ec21a2)

# Mátrix létrehozása
Ez a függvény hozza létre az üres mátrixot

![kép](https://github.com/user-attachments/assets/80715f5a-4ae0-4f20-b017-f354c5d39b9c)


# Az input érvényességének ellenőrzése
Ez a függvény ellenőrzi hogy a felhasználó által megadott input helyes-e (A sor és oszlop maximum értéke csak 10 és hogy a megadott pozíció még üres-e). A függvény paraméterei a felhasználó által megadott pozíció, a játék végét ellenőrző boolean és a regisztrálni kívánt karakter

![kép](https://github.com/user-attachments/assets/9fc6909b-8733-41c1-825c-566ff6332bc5)

# Változók Deklarálása és játéktér megjelenítése
A változók deklarálása, az üres mátrix létrehozása, nyerési minták megszabása, lépéseket számláló változó létrehozása, és a játéktér megjelnítése

![kép](https://github.com/user-attachments/assets/f78e78b2-883b-475a-8b3d-32c35b7753e7)

# Fő loop
Ez a loop a fő játékmenet, a pozíciók bekérése és a szükséges függvények meghívása itt történik

![kép](https://github.com/user-attachments/assets/46321808-ddbc-4376-973d-49b5d4a2c691)


# Egyéb megjegyzés
A pogram során a vege boolean a legtöbb függvényben szerepel a paraméterekben

Az importálható modul amit használtunk az os modul Ebből az os.system('cls') parancsot használtuk amely letísztítja a terminált és az os.get_terminal_size() parancsot ami megadja a terminál szélességét ez a középreigazítás szempontjából volt fontos. A megjelenítés során történik meg a terminál letiszítása és a játéktér középre igazítása így ha a játéktér változna akkor a megjelenítést követően ismét középen lesz a játéktér.

![kép](https://github.com/user-attachments/assets/62cbe132-f9e4-4eb7-96de-d3e42d7ce16d)
![kép](https://github.com/user-attachments/assets/707080fe-111e-4d5a-a56b-413b5e4f7c83)

![kép](https://github.com/user-attachments/assets/ca81aedb-cf2b-415d-9360-2ea2caaad78c)
![kép](https://github.com/user-attachments/assets/feaaffca-827b-4228-ab2f-db953e8a2a9d)




# Játék Használata
A játékban a koordinátákat vesszővel és egy space-el elválasztva kell megadni a minta szerint: sor, oszlop [példa: 4, 5 (Ez a 4. sor 5. oszlopát jelenti)]

![kép](https://github.com/user-attachments/assets/ea0e12e1-592a-4c4c-ba5a-9aba295623c9)




