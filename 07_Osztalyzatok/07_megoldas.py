jegyek = [5, 4, 3, 5, 2, 4, 4, 5, 3, 1, 4, 5, 3, 4, 2]

atlag = round(sum(jegyek) / len(jegyek), 2)
print(f"2. feladat: Az átlag: {atlag:.2f}")

keresett = int(input("3. feladat: Melyik jegyet keresi? "))
darab = jegyek.count(keresett)
print(f"A(z) {keresett}-es jegyből {darab} darab van.")

if 1 in jegyek:
    sorszam = jegyek.index(1) + 1
    print(f"4. feladat: Az első elégtelen jegy sorszáma: {sorszam}.")
else:
    print("4. feladat: Nem volt elégtelen jegy.")