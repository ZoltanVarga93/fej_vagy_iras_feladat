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

if tipp == random_erme_dobas:
    print("Ön eltalálta!")

if tipp != random_erme_dobas:
    print("Ön nem találta el!")

#3. feladat---------------------------------------------------------------------

txt = open(r'..\fej_vagy_iras_feladat\kiserlet.txt', 'r')
sor = txt.readline()
sorok_szama = 0

while sor != "":
    sor = txt.readline()
    sorok_szama += 1

print("3. feladat")
print(f"A kísérlet {sorok_szama} dobásból állt.")
txt.close()

#4. feladat---------------------------------------------------------------------

txt = open(r'..\fej_vagy_iras_feladat\kiserlet.txt', 'r')
sor = txt.readline()
fejek_szama = 0

while sor != "":
    if sor == "F\n":
        fejek_szama += 1
    sor = txt.readline()

print("4. feladat")
print(f'A kísérlet során a fej relatív gyakorisága {round(fejek_szama/sorok_szama*100,2)}% volt.')
txt.close()

#5. feladat---------------------------------------------------------------------

txt = open(r'..\fej_vagy_iras_feladat\kiserlet.txt', 'r')
sor = txt.readline()
ket_fej = 0
jo = True

while sor != "":
    if sor == "F\n" and jo == True:
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
    if maximum < fejek_sorozata:
        kezdet = sorok_szama-maximum
    max_lista.append(fejek_sorozata)
    maximum = max(max_lista)

print("6. feladat")
print(f'A leghosszabb tisztafej sorozat {maximum} tagból áll, kezdete a(z) {kezdet}. dobás.')
txt.close()

#7. feladat---------------------------------------------------------------------

ezres_lista = []
fej_kovette = 0
iras_kovette = 0

for i in range(250):

    random_erme_dobas_1 = random.choice(['I', 'F'])
    random_erme_dobas_2 = random.choice(['I', 'F'])
    random_erme_dobas_3 = random.choice(['I', 'F'])
    random_erme_dobas_4 = random.choice(['I', 'F'])

    ezres_lista.append([random_erme_dobas_1, random_erme_dobas_2, random_erme_dobas_3,random_erme_dobas_4])


for j in range(250):
    if ezres_lista[j][0] == 'F' and ezres_lista[j][1] == 'F' and ezres_lista[j][2] == 'F' and ezres_lista[j][3] == 'F':
        fej_kovette += 1
    if ezres_lista[j][0] == 'F' and ezres_lista[j][1] == 'F' and ezres_lista[j][2] == 'F' and ezres_lista[j][3] == 'I':
        iras_kovette += 1

dobasok = open(r'..\fej_vagy_iras_feladat\dobasok.txt', 'w')
dobasok.write(f'FFFF: {fej_kovette},FFFI: {iras_kovette}\n')

for k in range(250):
    dobasok.write(f'{ezres_lista[k][0]}{ezres_lista[k][1]}{ezres_lista[k][2]}{ezres_lista[k][3]} ')

dobasok.close()

input("Enter megnyomására bezáródik a program...")