# Gyakorlófeladat 9 – Parkoló

*Nehézség: ★★★★☆ – Digitális kultúra, középszintű érettségi programozási feladat szintje, Python nyelven.*

Egy parkolóház nap közbeni eseményeit rögzítették időrendben: **E** = egy autó érkezik, **T** = egy autó távozik. A 16 esemény az `esemenyek.txt` fájlban található:

```
E,E,E,T,E,E,E,E,T,E,T,T,E,E,E,T
```

A parkoló reggel üres. Ha egy autó érkezik, de nincs szabad férőhely, **elutasítják**, és nem áll be. Feltételezheti, hogy üres parkolóból autó nem távozik.

Írjon programot, amely az alábbi feladatokat oldja meg!

1. Tárolja el az eseményeket egy megfelelő adatszerkezetben a program forráskódjában, majd kérje be a billentyűzetről a parkoló férőhelyeinek számát! A bekérés előtt jelenjen meg a minta szerinti felirat!
2. Szimulálja a napot, és írja ki, hány autó áll a parkolóban a nap végén, és hány autót utasítottak el összesen!
3. Írja ki, hányadik eseménynél (1-től számozva) utasították el először az érkező autót! Ha senkit nem utasítottak el, a „Senkit nem utasítottak el.” üzenetet írja ki!
4. Határozza meg és írja ki a legnagyobb egyidejű foglaltságot, valamint azt, hogy a nap végén a férőhelyek hány százaléka volt foglalt (egy tizedesjegyre kerekítve)!
5. **Leadás.** A megoldását **GitHubon keresztül** kell leadnia: töltse fel a `parkolo.py` fájlt egy GitHub repositoryba, majd a **repository URL-jét** (pl. `https://github.com/felhasznalonev/repository-neve`) töltse fel a **Google Classroom** megfelelő feladatához! Más módon (e-mail, pendrive, csatolt fájl) leadott megoldást nem fogadunk el.

**Minta a szöveges kimenet kialakításához** (a bemenet: `4`):

```
1. feladat: Férőhelyek száma: 4
2. feladat: A nap végén 3 autó áll bent, 3 autót utasítottak el.
3. feladat: Az első elutasítás a(z) 7. eseménynél történt.
4. feladat: Legnagyobb foglaltság: 4, a nap végén 75.0%-ban volt tele.
```

Ha a férőhelyek száma `10`, a 3. feladat kimenete: `3. feladat: Senkit nem utasítottak el.`

## Általános tudnivalók

- A program forráskódját **`parkolo.py`** néven mentse!
- Az adatokat a program forráskódjában, **listában** tárolja. A(z) `esemenyek.txt` fájl tartalmát a kódba másolhatja, a programnak fájlt **nem** kell (és nem szabad) beolvasnia.
- A felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie.
- A programnak akkor is helyesen kell működnie, ha az adatokat a kódban kicseréljük (más elemszám, más értékek), illetve más férőhelyszámot adunk meg, ezért ne írjon a programba előre kiszámolt eredményt vagy az elemszámot rögzítő számot!
- A képernyőre írást igénylő feladatoknál az ékezet nélküli kiírás is elfogadott.
- A minta szerint írja ki a feladat sorszámát (pl. `2. feladat:`), majd a kiírt tartalomra utaló szöveget!
- A megjegyzésben (kommentben) elhelyezett kód vagy szöveg nem értékelhető.
- Ajánlott megoldási idő: **30 perc**. Összesen **15 pont** szerezhető.
