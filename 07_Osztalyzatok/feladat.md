# Gyakorlófeladat 7 – Osztályzatok

*Nehézség: ★★☆☆☆ – Digitális kultúra, középszintű érettségi programozási feladat szintje, Python nyelven.*

Egy diák 15 érdemjegyet kapott egy tanév során (1 = elégtelen, 5 = jeles). A jegyeket a `jegyek.txt` fájl tartalmazza:

```
5,4,3,5,2,4,4,5,3,1,4,5,3,4,2
```

Írjon programot, amely az alábbi feladatokat oldja meg!

1. Tárolja el a 15 jegyet egy megfelelő adatszerkezetben a program forráskódjában!
2. Határozza meg és írja ki a jegyek átlagát két tizedesjegyre kerekítve!
3. Kérjen be a billentyűzetről egy jegyet (1–5)! A bekérés előtt jelenjen meg a minta szerinti felirat! Írja ki, hány darab ilyen jegye van a diáknak!
4. Keresse meg az első elégtelen (1-es) jegyet, és írja ki a sorszámát (1-től számozva)! Ha nincs elégtelen jegy, a „Nem volt elégtelen jegy.” üzenetet írja ki!
5. **Leadás.** A megoldását **GitHubon keresztül** kell leadnia: töltse fel a `osztalyzatok.py` fájlt egy GitHub repositoryba, majd a **repository URL-jét** (pl. `https://github.com/felhasznalonev/repository-neve`) töltse fel a **Google Classroom** megfelelő feladatához! Más módon (e-mail, pendrive, csatolt fájl) leadott megoldást nem fogadunk el.

**Minta a szöveges kimenet kialakításához** (a bemenet: `4`):

```
2. feladat: Az átlag: 3.60
3. feladat: Melyik jegyet keresi? 4
A(z) 4-es jegyből 5 darab van.
4. feladat: Az első elégtelen jegy sorszáma: 10.
```

Ha a bekért jegy `3`, a kiírás: `A(z) 3-es jegyből 3 darab van.`

## Általános tudnivalók

- A program forráskódját **`osztalyzatok.py`** néven mentse!
- Az adatokat a program forráskódjában, **listában** tárolja. A(z) `jegyek.txt` fájl tartalmát a kódba másolhatja, a programnak fájlt **nem** kell (és nem szabad) beolvasnia.
- A felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie.
- A programnak akkor is helyesen kell működnie, ha az adatokat a kódban kicseréljük (más elemszám, más értékek), ezért ne írjon a programba előre kiszámolt eredményt vagy az elemszámot rögzítő számot!
- A képernyőre írást igénylő feladatoknál az ékezet nélküli kiírás is elfogadott.
- A minta szerint írja ki a feladat sorszámát (pl. `2. feladat:`), majd a kiírt tartalomra utaló szöveget!
- A megjegyzésben (kommentben) elhelyezett kód vagy szöveg nem értékelhető.
- Ajánlott megoldási idő: **25 perc**. Összesen **15 pont** szerezhető.
