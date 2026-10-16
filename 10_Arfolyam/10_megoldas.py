arfolyamok = [320, 335, 331, 340, 352, 347, 360, 358, 341, 345, 362, 370]

emelkedett = 0
csokkent = 0

for i in range(1, len(arfolyamok)):
    if arfolyamok[i] > arfolyamok[i - 1]:
        emelkedett += 1
    elif arfolyamok[i] < arfolyamok[i - 1]:
        csokkent += 1

print(f"2. feladat: Emelkedett: {emelkedett} napon, csökkent: {csokkent} napon.")

max_csokkenes = 0 
max_csokkenes_nap = 0

for i in range(1, len(arfolyamok)):
    csokkenes = arfolyamok[i - 1] - arfolyamok[i]
    if csokkenes > max_csokkenes:
        max_csokkenes = csokkenes
        max_csokkenes_nap = i + 1

print(f"3. feladat: A legnagyobb esés: {max_csokkenes} Ft a(z) {max_csokkenes_nap}. napon.")

kuszob = int(input("4. feladat: Küszöb (Ft): "))

kuszob_nap = None
for i in range(len(arfolyamok)):
    if arfolyamok[i] > kuszob:
        kuszob_nap = i + 1
        break

if kuszob_nap is not None:
    print(f"Az első nap, amikor az árfolyam meghaladta a küszöböt: {kuszob_nap}.")
else:
    print("Az árfolyam nem haladta meg a küszöböt.")