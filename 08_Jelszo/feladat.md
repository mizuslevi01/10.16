# Gyakorlófeladat 8 – Jelszó

*Nehézség: ★★★☆☆ – Digitális kultúra, középszintű érettségi programozási feladat szintje, Python nyelven.*

Egy weboldal regisztrációjánál ellenőrizni kell a megadott jelszó erősségét. Egy jelszó **erős**, ha legalább 8 karakter hosszú, és tartalmaz kisbetűt, nagybetűt és számjegyet is. Ennél a feladatnál nincs forrásfájl, az adatot a felhasználó adja meg.

Írjon programot, amely az alábbi feladatokat oldja meg!

1. Kérje be a billentyűzetről a jelszót! A bekérés előtt jelenjen meg a minta szerinti felirat!
2. Határozza meg és írja ki, hány kisbetű, nagybetű, számjegy és egyéb (nem betű és nem számjegy) karakter van a jelszóban!
3. Írja ki a jelszó hosszát és az első számjegy helyét (1-től számozva)! Ha nincs számjegy a jelszóban, ezt az üzenetet írja ki: „Nincs számjegy a jelszóban.”
4. Döntse el, hogy a jelszó erős-e! Ha igen, az „Erős jelszó.”, különben a „Gyenge jelszó.” üzenetet írja ki!
5. **Leadás.** A megoldását **GitHubon keresztül** kell leadnia: töltse fel a `jelszo.py` fájlt egy GitHub repositoryba, majd a **repository URL-jét** (pl. `https://github.com/felhasznalonev/repository-neve`) töltse fel a **Google Classroom** megfelelő feladatához! Más módon (e-mail, pendrive, csatolt fájl) leadott megoldást nem fogadunk el.

**Minta a szöveges kimenet kialakításához** (a bemenet: `Alma2024Kert!`):

```
1. feladat: Jelszó: Alma2024Kert!
2. feladat: Kisbetű: 6, nagybetű: 2, számjegy: 4, egyéb: 1
3. feladat: A jelszó hossza: 13, az első számjegy a(z) 5. helyen van.
4. feladat: Erős jelszó.
```

Ha a jelszó `alma123`, a 4. feladat kimenete: `4. feladat: Gyenge jelszó.`

## Általános tudnivalók

- A program forráskódját **`jelszo.py`** néven mentse!
- Az adatot a program a billentyűzetről kéri be, fájlt **nem** kell (és nem szabad) beolvasnia.
- A felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie.
- A programnak akkor is helyesen kell működnie, ha más hosszúságú és tartalmú jelszót adunk meg, ezért ne írjon a programba előre kiszámolt eredményt vagy az elemszámot rögzítő számot!
- A képernyőre írást igénylő feladatoknál az ékezet nélküli kiírás is elfogadott.
- A minta szerint írja ki a feladat sorszámát (pl. `2. feladat:`), majd a kiírt tartalomra utaló szöveget!
- A megjegyzésben (kommentben) elhelyezett kód vagy szöveg nem értékelhető.
- Ajánlott megoldási idő: **25 perc**. Összesen **15 pont** szerezhető.
