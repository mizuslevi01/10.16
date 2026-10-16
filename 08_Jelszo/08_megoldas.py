jelszo = input("1. feladat: Jelszó: ")

kisbetu = 0
nagybetu = 0
szam = 0
egyeb = 0

for karakter in jelszo:
    if karakter.islower():
        kisbetu += 1
    elif karakter.isupper():
        nagybetu += 1
    elif karakter.isdigit():
        szam += 1
    else:
        egyeb += 1

print(f"2. feladat: Kisbetű: {kisbetu}, nagybetű: {nagybetu}, számjegy: {szam}, egyéb: {egyeb}")

elso_szam_hely = None
for i in range(len(jelszo)):
    if jelszo[i].isdigit():
        elso_szam_hely = i + 1
        break

if elso_szam_hely is not None:
    print(f"3. feladat: A jelszó hossza: {len(jelszo)}, az első számjegy a(z) {elso_szam_hely}. helyen van.")
else:
    print(f"3. feladat: A jelszó hossza: {len(jelszo)}, Nincs számjegy a jelszóban.")

if len(jelszo) >= 8 and kisbetu > 0 and nagybetu > 0 and szam > 0:
    print("4. feladat: Erős jelszó.")
else:
    print("4. feladat: Gyenge jelszó.")