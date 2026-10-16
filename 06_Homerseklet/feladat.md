# Gyakorlófeladat 6 – Hőmérséklet

*Nehézség: ★☆☆☆☆ – Digitális kultúra, középszintű érettségi programozási feladat szintje, Python nyelven.*

Egy meteorológiai állomás 10 egymást követő nap reggeli hőmérsékletét mérte °C-ban. Az adatokat a `homerseklet.txt` fájl tartalmazza:

```
3,-2,-5,0,4,7,-1,2,-4,8
```

Írjon programot, amely az alábbi feladatokat oldja meg!

1. Tárolja el a 10 napi hőmérsékletet egy megfelelő adatszerkezetben a program forráskódjában!
2. Határozza meg és írja ki az átlaghőmérsékletet egy tizedesjegyre kerekítve!
3. Határozza meg és írja ki a legalacsonyabb hőmérsékletet és azt, hogy hányadik napon mérték! Ha több ilyen nap van, az elsőt adja meg! A napokat 1-től számozzuk.
4. Határozza meg és írja ki, hány napon volt fagy (0 °C alatti hőmérséklet)!
5. **Leadás.** A megoldását **GitHubon keresztül** kell leadnia: töltse fel a `homerseklet.py` fájlt egy GitHub repositoryba, majd a **repository URL-jét** (pl. `https://github.com/felhasznalonev/repository-neve`) töltse fel a **Google Classroom** megfelelő feladatához! Más módon (e-mail, pendrive, csatolt fájl) leadott megoldást nem fogadunk el.

**Minta a szöveges kimenet kialakításához:**

```
2. feladat: Az átlaghőmérséklet: 1.2 °C
3. feladat: A leghidegebb nap: 3. nap, -5 °C
4. feladat: 4 napon volt fagy.
```

## Általános tudnivalók

- A program forráskódját **`homerseklet.py`** néven mentse!
- Az adatokat a program forráskódjában, **listában** tárolja. A(z) `homerseklet.txt` fájl tartalmát a kódba másolhatja, a programnak fájlt **nem** kell (és nem szabad) beolvasnia.
- A felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie.
- A programnak akkor is helyesen kell működnie, ha az adatokat a kódban kicseréljük (más elemszám, más értékek), ezért ne írjon a programba előre kiszámolt eredményt vagy az elemszámot rögzítő számot!
- A képernyőre írást igénylő feladatoknál az ékezet nélküli kiírás is elfogadott.
- A minta szerint írja ki a feladat sorszámát (pl. `2. feladat:`), majd a kiírt tartalomra utaló szöveget!
- A megjegyzésben (kommentben) elhelyezett kód vagy szöveg nem értékelhető.
- Ajánlott megoldási idő: **20 perc**. Összesen **15 pont** szerezhető.
