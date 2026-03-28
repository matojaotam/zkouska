[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/V_kze1P8)
# Analýza růstu buněk

Tato úloha simuluje jednoduchou datovou analýzu, se kterou by ses mohl(a) setkat například v laboratorní praxi.
Dostaneš naměřená data v čase, ověříš jejich vlastnosti a připravíš přehled výsledků, který může být dále použit například v reportu nebo pro vizualizaci.

Data představují velikosti buněčných vzorků měřené v jednotlivých časových intervalech.
V předchozím cvičení jsi již implementoval(a) funkci pro načtení těchto dat z CSV souboru. Na tuto část nyní navážeš.

Tvým úkolem bude analyzovat růst jednotlivých vzorků buněk a uložit výsledky do JSON souboru.
Ne všechny vzorky totiž rostou stejným způsobem – některé mají lineární růst (velikost se v každém kroku zvětšuje
o stejnou hodnotu), zatímco jiné mají růst nelineární.

Program bude postupovat v několika krocích:
1. Načte data ze souboru CSV (pomocí již implementované funkce).
2. Zkontroluje linearitu růstu a případně spočítá rychlost růstu.
3. Vytvoří přehled základních statistik pro každý vzorek.
4. Výsledky uloží do souboru ve formátu JSON.

Řešení úkolu bude rozděleno do několika funkcí, které budeš implementovat v souboru `cells_analysis.py`.

---

## Vstupní data a jejich načtení

Vstupní soubor `samples.csv` obsahuje data o jednotlivých vzorcích buněk. 
Každý řádek představuje jeden vzorek buněk a má následující strukturu:

* **První hodnota** je název vzorku.
* **Další hodnoty** jsou velikosti buněk v jednotlivých časových intervalech.

Příklad souboru:

```csv
SampleA,10,12,14,16
SampleB,5,7,9,11
SampleC,3,4,6,8
SampleD,20,22,24,26
```

V souboru `cells_analysis.py` budeš pracovat s funkcí `load_samples()`, která tato data načte a převede do slovníku.

Výsledná datová struktura má mít tvar:
- klíče – názvy vzorků,
- hodnoty – seznamy čísel představující velikosti buněk v jednotlivých časových intervalech.

Například:
```python
{
    "SampleA": [10, 12, 14, 16],
    "SampleB": [5, 7, 9, 11]
}
```

Funkci `load_samples()` jsi již implementoval(a) na cvičení.

**Zkopíruj ji proto do souboru `cells_analysis.py` a před pokračováním v úloze si ověř, že správně načítá data ze souboru `samples.csv`.**

---

# Úkol 1: Kontrola lineárního růstu

Vytvoř funkci `calculate_growth_rate()`.
* Funkce přijímá jeden vstupní parametr - seznam představující velikosti jednoho vzorku v jednotlivých časových intervalech (např. `[10, 12, 14, 16]`).
* Funkce zkontroluje, zda vzorek roste lineárně. To znamená, že spočítá rozdíly mezi po sobě jdoucími hodnotami a zkontroluje, zda jsou všechny rozdíly stejné.
    * Pokud **nejsou všechny rozdíly stejné**, jedná se o **nelineární růst** a funkce vrátí `None`.
    * Pokud je růst **lineární**, funkce spočítá průměrnou rychlost růstu a vrátí ji jako číslo.
* Pro vzorek `"SampleA"` z příkladu by funkce vrátila `2`, protože rozdíly mezi hodnotami jsou všechny `2` (12-10, 14-12, 16-14).
* Pro vzorek `"SampleC"` by funkce vrátila `None`, protože rozdíly mezi hodnotami nejsou stejné (4-3=1, 6-4=2, 8-6=2).

---

# Úkol 2: Vytvoření přehledu vzorku

Vytvoř funkci `create_sample_summary()`:
* Funkce přijímá dva vstupní parametry:
    * `values` - seznam představující velikosti jednoho vzorku v jednotlivých časových intervalech (např. `[10, 12, 14, 16]`),
    * `growth_rate` - rychlost růstu (výstup z `calculate_growth_rate()`).
* Funkce vrátí přímo slovník statistik pro jeden vzorek s klíči:
  * `"values"` - původní hodnoty vzorku,
  * `"average"` - průměrná velikost vzorku,
  * `"min"` - minimální hodnota,
  * `"max"` - maximální hodnota,
  * `"growth_rate"` - rychlost růstu.
  * Například pro vzorek "SampleA" bude přehled vypadat takto:

  ```python
  {
  "values": [10, 12, 14, 16],
  "average": 13,
  "min": 10,
  "max": 16,
  "growth_rate": 2
  }
  ```

---

# Úkol 3: Uložení výsledků

Vytvoř funkci `save_results()`.
* Funkce přijímá dva vstupní parametry:
    * `summary` - slovník s přehledem všech vzorků (výstup z `create_sample_summary()` pro všechny vzorky, viz Úkol 4),
    * `filename` - název souboru, do kterého se mají výsledky uložit (např. `results.json`).
* Funkce převádí vstupní slovník do formátu JSON a uloží ho do souboru s názvem `filename`.
* Při ukládání použij formátování pro lepší čitelnost (např. `indent=4`).
* Funkce nevrací žádnou hodnotu, pouze uloží soubor.

---

# Úkol 4: Hlavní program

Vytvoř funkci `main()`, která bude koordinovat celý proces:
* Funkce nepřijímá žádné vstupní parametry.
* Funkce načte data ze souboru `samples.csv` (úkol ze cvičení 5).
* Funkce pro každý vzorek ze souboru provede:
  * Kontrolu lineárního růstu a výpočet rychlosti růstu (úkol 1).
  * Vytvoření přehledu se statistikami (úkol 2).
  * Uložení výsledků do slovníku `summary`, kde klíči jsou názvy vzorků a hodnotami jsou přehledy vytvořené v úkolu 2.
* Nakonec funkce uloží výsledky do souboru `results.json` pomocí `save_results()` (úkol 3).

---

### Spouštění programu
- Spouštění programu prováděj v souboru `cells_analysis.py` v podmínce `if __name__ == "__main__":`, např.:

  ```python
  if __name__ == "__main__":
      main()
      print("Analýza buněk dokončena. Výsledky uloženy do results.json.")
  ```

### Testování řešení
- Hlavní ověření řešení probíhá po odeslání na GitHub Classroom, kde se automaticky spustí testy.
- Pro rychlejší kontrolu před odesláním můžeš testy spouštět lokálně:
  - všechny testy: `uv run pytest`
  - jeden test soubor: `uv run pytest .\tests\test_load_samples.py`
  - (v případě potřeby nejdřív synchronizuj prostředí příkazem `uv sync`)
- Doporučený postup řešení:
  1. Pro každou funkci si připrav ukázkový vstup pro rychlé testování.
  2. Logiku si nejdřív vyzkoušej jako jednoduchý skript.
  3. Funkční kód zabal do funkce a ověř ho zavoláním funkce s ukázkovým vstupem.
  4. Spusť automatický test pro danou funkci (např. `uv run pytest .\tests\test_load_samples.py`).
  5. Na další funkci přejdi až ve chvíli, kdy aktuální funkce prochází testem.
