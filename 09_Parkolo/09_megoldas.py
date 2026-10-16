esemenyek = ["E", "E", "E", "T", "E", "E", "E", "E", "T", "E", "T", "T", "E", "E", "E", "T"]

ferohely = int(input("1. feladat: Férőhelyek száma: "))

bent = 0
elutasitva = 0
elso_elutasitas = None
max_foglalt = 0

for i, esemeny in enumerate(esemenyek, 1):
    if esemeny == "E":
        if bent < ferohely:
            bent += 1
            if bent > max_foglalt:
                max_foglalt = bent
        else:
            elutasitva += 1
            if elso_elutasitas is None:
                elso_elutasitas = i
    elif esemeny == "T":
        if bent > 0:
            bent -= 1

print(f"2. feladat: A nap végén {bent} autó áll bent, {elutasitva} autót utasítottak el.")

if elso_elutasitas is not None:
    print(f"3. feladat: Az első elutasítás a(z) {elso_elutasitas}. eseménynél történt.")
else:
    print("3. feladat: Senkit nem utasítottak el.")

szazalek = round((bent / ferohely) * 100, 1)
print(f"4. feladat: Legnagyobb foglaltság: {max_foglalt}, a nap végén {szazalek:.1f}%-ban volt tele.")