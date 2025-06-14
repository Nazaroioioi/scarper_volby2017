```
# 🗳️ Projekt 3 – Scraper volebních výsledků (PSP 2017)

**Autor:** [DOPLň SVÉ JMÉNO]  
**Email:** [DOPLň EMAIL]  
**Discord:** [DOPLň DISCORD]

## Popis projektu

Tento projekt slouží ke stažení výsledků parlamentních voleb z roku 2017 v České republice z webu [volby.cz](https://www.volby.cz/).  
Skript získá podrobné výsledky hlasování pro všechny obce ve zvoleném územním celku a výstup uloží do CSV souboru.

---

## 📦 Instalace

Nejprve si vytvoř virtuální prostředí (např. pomocí `venv`):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

Nainstaluj požadované knihovny pomocí `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## ▶️ Spuštění skriptu

Skript se spouští ze souboru `projekt_3.py` a vyžaduje **2 argumenty**:

1. URL odkazu na územní celek (např. okres Prostějov)
2. Název výstupního CSV souboru

### Ukázka:

```bash
python projekt_3.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" vysledky_prostejov.csv
```

---

## 📁 Výstup

Výstupní CSV soubor obsahuje jeden řádek pro každou obec s následujícími údaji:

- Kód obce
- Název obce
- Počet voličů v seznamu
- Počet vydaných obálek
- Počet platných hlasů
- Hlasy pro jednotlivé politické strany

Ukázka řádku výstupu:

```
503160, Bedihošť, 1436, 957, 948, ANO 2011: 368, ODS: 152, ...
```

---

## 📄 Obsah repozitáře

- `projekt_3.py` – hlavní skript pro scraping
- `requirements.txt` – seznam potřebných knihoven
- `README.md` – tento soubor s dokumentací
- `vysledky_prostejov.csv` – ukázkový výstup

---

## 🚲 Použité knihovny

- `requests`
- `beautifulsoup4`
```

---

requirements.txt
```
requests
beautifulsoup4
```

---

projekt_3.py (přidáná hlavička)
```
"""
projekt_3.py: třetí projekt  

author: [DOPLň SVÉ JMÉNO]  
email: [DOPLň EMAIL]  
discord: [DOPLň DISCORD]
"""

import requests
from bs4 import BeautifulSoup
import csv
import sys
...
