import random

#1. feladat---------------------------------------------------------------------

random_erme_dobas = random.choice(['I','F'])
print("1. feladat")
print("A pénzfeldobás eredménye:", random_erme_dobas)

#2. feladat---------------------------------------------------------------------

print("2. feladat")
tipp = input("Tippeljen! (F/I)= ")
random_erme_dobas = random.choice(['I','F'])
print(f'A tipp {tipp}, a dobás eredménye {random_erme_dobas} volt')

if tipp == random_erme_dobas: # Nem rossz, de ilyenkor (két kizáró kimenetel) rövidebb egy if-else elágazáspár....
    print("Ön eltalálta!")

if tipp != random_erme_dobas:
    print("Ön nem találta el!")

#3. feladat---------------------------------------------------------------------

txt = open(r'..\fej_vagy_iras_feladat\kiserlet.txt', 'r')
sor = txt.readline() # a fájl minden sorában egy kísérlet van (nincs fejléc), ezzel elveszítesz egy adatot (a 0. sort)
sorok_szama = 0

while sor != "":
    sor = txt.readline()
    sorok_szama += 1

print("3. feladat")
print(f"A kísérlet {sorok_szama} dobásból állt.")
txt.close()

#4. feladat---------------------------------------------------------------------
# igen, jól csinálod, hogy mindig újranyitod a fájlt hiszen nem szabad most letárolni pl. listában az adatokat, 
# ugyanakkor ez a feladat összevonható az előzővel, pl. a sorok mellett számolhattad volna a fejeket is (érdemes előbb kidolgozni papíron a feladat megoldását, sémáját, és utána lekódolni)
txt = open(r'..\fej_vagy_iras_feladat\kiserlet.txt', 'r')
sor = txt.readline()
fejek_szama = 0

while sor != "":
    if sor == "F\n":
        fejek_szama += 1
    sor = txt.readline()

print("4. feladat")
print(f'A kísérlet során a fej relatív gyakorisága {round(fejek_szama/sorok_szama*100,2)}% volt.') # sorok_száma=általad_számolt + 1!
txt.close()

#5. feladat---------------------------------------------------------------------
# ez a megoldás biztosan minden esetben működik? 
# -> általános "programozási tétel": túl sok (3+) egymásba ágyazott elágazást kerülni kell, 
# általában ilyenkor van alternatíva, ugyanakkor megnehezíti a programkód olvashatóságát a túl sok feltételes elágazás egymásban, könnyű hibázni, nehéz bővíteni...
txt = open(r'..\fej_vagy_iras_feladat\kiserlet.txt', 'r')
sor = txt.readline()
ket_fej = 0
jo = True

# alternatív mo.: 
    # Ha ez a sor fej: addig olvasunk, amíg a köv. sor fej közben számoljuk a fejeket, 
        # írásnál kilépünk és ha kettő fejet számolt, akkor elmentjük
while sor != "":
    if sor == "F\n" and jo == True: # ez a sor így is írható: if sor == "F\n" and jo:
        # a boolean típusú értékeket felesleges már logikai vizsgálat alá vetni, hiszen logikai értékük van! (minden programnyelvben: True == True -> True)
        sor = txt.readline()
        if sor == "F\n":
            sor = txt.readline()
            if sor != "F\n":
                ket_fej += 1
            else:
                jo = False
        else:
            jo = False
    if sor == "I\n":
        jo = True
    sor = txt.readline()

print("5. feladat")
print(f'A kísérlet során {ket_fej} alkalommal dobtak pontosan két fejet egymás után')
txt.close()

#6. feladat---------------------------------------------------------------------

txt = open(r'..\fej_vagy_iras_feladat\kiserlet.txt', 'r')
sor = txt.readline()
sorok_szama = 1
fejek_sorozata = 0
max_lista = []
maximum = 0
kezdet = 0

while sor != "":
    sor = txt.readline()
    sorok_szama += 1

    if sor == "I\n":
        fejek_sorozata = 0
    if sor == "F\n":
        fejek_sorozata += 1
    if maximum < fejek_sorozata: # ezt a feltételt elegendő lenne: 'sor == "F\n":'-ben nézni, felesleges minden lépésben, amikor 'I\n'-van...
        kezdet = sorok_szama-maximum
    max_lista.append(fejek_sorozata) # ugyanez, nem kell mindig appendálni, elegendő, csak ha pl. találtunk az eddigi max hossznál hosszabb sort
    maximum = max(max_lista)  # ugyanez, folyamatosan, 1-elemmel bővülő listában mindig újrakeresni a max-ot elég erőforrás pocsékoló

print("6. feladat")
print(f'A leghosszabb tisztafej sorozat {maximum} tagból áll, kezdete a(z) {kezdet}. dobás.')
txt.close()

#7. feladat---------------------------------------------------------------------

ezres_lista = []
fej_kovette = 0
iras_kovette = 0

for i in range(250): # 1 000 db 4-dobásos sorozat kell, összesen: 4 000 dobás (F/I)

    random_erme_dobas_1 = random.choice(['I', 'F'])
    random_erme_dobas_2 = random.choice(['I', 'F'])
    random_erme_dobas_3 = random.choice(['I', 'F'])
    random_erme_dobas_4 = random.choice(['I', 'F'])
    # már itt az appendálásnál lehetne ellenőrözni, hogy az utolsó elem F/I, a másik for-megspórolható!
    ezres_lista.append([random_erme_dobas_1, random_erme_dobas_2, random_erme_dobas_3,random_erme_dobas_4]) # tuple-ként érdemesebb tárolni a 4-es sorozatokat!


for j in range(250):
    # Megjegyzések: ------------------------------------------------------------------------
    # ilyen if-ekre egy trükk: nekünk két esetet kell megkülönböztetni, F/I -> cseréljük le F-et: True, I-t: False-ra!, csak a fáljba írásnál kell F-et és I-t írni helyettük
    # ekkor FFFI : True True True False
    #       FFFF : True True True True
    # szeretünk boolean típussal dolgozni, mert 2-állapotú, kevés helyet foglal (1 bit), logikai maszkolást lehet végezni velük, könnyű feltételt írni stb...  
    # pl. ezek után tetszőleges sorozatot kérhetne a feladat:
    # FFIIFFFII :  mask = (True, True, False, False, True, True, True, False, False) (mint maszk szolgál, tuple-ként)
    #
    # 
    # XOR-operátor (Python-ban: ^): akkor ad True-t, ha a két bemeneti érték NEM EGYEZIK MEG: 
    # True ^ True = False,
    # False ^ False = False,
    # False ^ True = True
    # True ^ False = True
    #
    # jo_ez_a_sorozat = True
    # for i in range(len(random_9_elemu_sorozat)):
    #   jo_ez_a_sorozat = jo_ez_a_sorozat and not(random_9_elemu_sorozat[i] ^ mask[i])
    #
    # if jo_ez_a_sorozat:
    #   print('Eltaláltunk egy kívánt sorozatot: {mask}!')
    #
    #-----------------------------------------------------------------------------------------
    # az_eleje_csupa_fej = True
    # for elemindex in range(3): -> 0, 1, 2,
    #    az_eleje_csupa_fej = az_eleje_csupa_fej and ezres_lista[j][elemindex]
    #
    # if az_eleje_csupa_fej:
    #   if ezres_lista[j][-1]: -> az utolsó elemre fókuszálunk, ha True akkor F, egyébként I
    #       fej_kovette += 1
    #   else:
    #       iras_kovette += 1
    
    if ezres_lista[j][0] == 'F' and ezres_lista[j][1] == 'F' and ezres_lista[j][2] == 'F' and ezres_lista[j][3] == 'F':
        fej_kovette += 1
    if ezres_lista[j][0] == 'F' and ezres_lista[j][1] == 'F' and ezres_lista[j][2] == 'F' and ezres_lista[j][3] == 'I':
        iras_kovette += 1

dobasok = open(r'..\fej_vagy_iras_feladat\dobasok.txt', 'w')
dobasok.write(f'FFFF: {fej_kovette},FFFI: {iras_kovette}\n')

for k in range(250):
    dobasok.write(f'{ezres_lista[k][0]}{ezres_lista[k][1]}{ezres_lista[k][2]}{ezres_lista[k][3]} ')
    # rövidebb:  
    # dobasok.write(f'{''.join(ezres_lista[k])} ')

dobasok.close()

input("Enter megnyomására bezáródik a program...") # pontosabban bármilyen gomb lenyomására, de konzolos alkalmazásokhoz ez egy jó módszer :-)
