adatok = [3, -2, -5, 0, 4, 7, -1, 2, -4, 8]

atlag = round(sum(adatok) / len(adatok), 1)
print(f"2. feladat: Az átlaghőmérséklet: {atlag} °C")

min_temp = min(adatok)
min_nap = adatok.index(min_temp) + 1
print(f"3. feladat: A leghidegebb nap: {min_nap}. nap, {min_temp} °C")

fagynapok = 0
for homerseklet in adatok:
    if homerseklet < 0:
        fagynapok += 1

print(f"4. feladat: {fagynapok} napon volt fagy.")