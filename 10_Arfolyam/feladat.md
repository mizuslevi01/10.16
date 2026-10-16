# Gyakorlófeladat 10 – Árfolyam

*Nehézség: ★★★★★ (a középszint felső határa) – Digitális kultúra, középszintű érettségi programozási feladat szintje, Python nyelven.*

Egy részvény 12 egymást követő napi záróárfolyamát forintban az `arfolyam.txt` fájl tartalmazza:

```
320,335,331,340,352,347,360,358,341,345,362,370
```

Írjon programot, amely az alábbi feladatokat oldja meg!

1. Tárolja el a 12 napi árfolyamot egy megfelelő adatszerkezetben a program forráskódjában!
2. A 2. naptól kezdve hasonlítsa össze mindegyik napi árfolyamot az előző napival! Írja ki, hány napon emelkedett és hány napon csökkent az árfolyam!
3. Határozza meg és írja ki a legnagyobb napi csökkenést (az előző napi árfolyam és a mai különbsége) és azt, hogy hányadik napon következett be! Ha több ilyen nap van, az elsőt adja meg! A napokat 1-től számozzuk. Feltételezheti, hogy volt legalább egy napi csökkenés.
4. Kérjen be a billentyűzetről egy küszöbértéket forintban! A bekérés előtt jelenjen meg a minta szerinti felirat! Írja ki, hányadik napon haladta meg először az árfolyam a küszöböt (a küszöbbel egyenlő érték még nem haladja meg)! Ha nem haladta meg, az „Az árfolyam nem haladta meg a küszöböt.” üzenetet írja ki!
5. **Leadás.** A megoldását **GitHubon keresztül** kell leadnia: töltse fel a `arfolyam.py` fájlt egy GitHub repositoryba, majd a **repository URL-jét** (pl. `https://github.com/felhasznalonev/repository-neve`) töltse fel a **Google Classroom** megfelelő feladatához! Más módon (e-mail, pendrive, csatolt fájl) leadott megoldást nem fogadunk el.

**Minta a szöveges kimenet kialakításához** (a bemenet: `350`):

```
2. feladat: Emelkedett: 7 napon, csökkent: 4 napon.
3. feladat: A legnagyobb esés: 17 Ft a(z) 9. napon.
4. feladat: Küszöb (Ft): 350
Az első nap, amikor az árfolyam meghaladta a küszöböt: 5.
```

## Általános tudnivalók

- A program forráskódját **`arfolyam.py`** néven mentse!
- Az adatokat a program forráskódjában, **listában** tárolja. A(z) `arfolyam.txt` fájl tartalmát a kódba másolhatja, a programnak fájlt **nem** kell (és nem szabad) beolvasnia.
- A felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie.
- A programnak akkor is helyesen kell működnie, ha az adatokat a kódban kicseréljük (más elemszám, más értékek), ezért ne írjon a programba előre kiszámolt eredményt vagy az elemszámot rögzítő számot!
- A képernyőre írást igénylő feladatoknál az ékezet nélküli kiírás is elfogadott.
- A minta szerint írja ki a feladat sorszámát (pl. `2. feladat:`), majd a kiírt tartalomra utaló szöveget!
- A megjegyzésben (kommentben) elhelyezett kód vagy szöveg nem értékelhető.
- Ajánlott megoldási idő: **30 perc**. Összesen **15 pont** szerezhető.
