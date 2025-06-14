readme

# Skript pro získávání výsledků voleb z volby.cz

Tento Python skript je navržen pro automatické stahování (scrapování) dat o výsledcích voleb z webu [volby.cz](https://www.volby.cz). Zaměřuje se na získání informací o obcích v konkrétním kraji a následně na podrobné údaje o počtu voličů, vydaných obálek a hlasech jednotlivých politických stran v každé obci. Shromážděná data jsou uložena do CSV souboru

## Co skript dělá?
1. **Načte úvodní stránku:** Skript začíná na přehledové stránce pro vybraný kraj a volby (URL je zadáno jako vstupní parametr).
2. **Získá ID a názvy obcí:** Z této stránky vytáhne číselné identifikátory (ID) a názvy všech obcí.
3. **Sbírá podrobné informace pro každou obec:** Pro každou obec načte její detailní stránku s výsledky.
4. **Získává data:** Z detailní stránky vytáhne:
   * Počet registrovaných voličů
   * Počet vydaných obálek
   * Počet platných hlasů
   * Jména politických stran a počet hlasů pro každou z nich
   * Automaticky ukládá všechny unikátní názvy stran, aby je mohl použít jako záhlaví sloupců v CSV.
5. **Ukládá výsledky do CSV:** Veškerá sesbíraná data jsou organizována a uložena do jednoho CSV souboru, jehož název je zadán jako vstupní parametr.

Tady máš mírně přeformulovanou verzi této části:

---

## Jak spustit skript

Skript se spouští z příkazové řádky a vyžaduje zadání dvou parametrů: URL stránky pro scrapování a název výstupního CSV souboru.

1. Uložte kód do souboru s příponou `.py` (například `volby_scraper.py`).
2. Ujistěte se, že ve stejném adresáři máte i soubor `requirements.txt`.
3. Otevřete terminál nebo příkazový řádek, přejděte do složky, kde je skript uložen, a spusťte ho pomocí:

```bash
python volby_scraper.py <URL_PRO_SCRAPOVANI> <NAZEV_VYSTUPNIHO_SOUBORU.csv>
```

### Příklad spuštění:

```bash
python volby_scraper.py https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103 vysledky_jihomoravsky_2017.csv
```

* URL `https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103` slouží ke scrapování dat (v tomto případě Jihomoravský kraj, volby 2017).
* `vysledky_jihomoravsky_2017.csv` je název souboru, kam se výsledky uloží. Skript automaticky zajistí, že soubor bude mít příponu `.csv`.

---

### Požadavky a instalace

Než skript spustíte, ujistěte se, že máte nainstalovány všechny potřebné knihovny. Tyto knihovny jsou uvedeny v souboru requirements.txt.

Pro instalaci všech závislostí otevřete terminál nebo příkazový řádek ve stejném adresáři jako váš skript a requirements.txt a spusťte následující příkaz:

bash
pip install -r requirements.txt
