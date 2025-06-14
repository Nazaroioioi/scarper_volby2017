import requests
from bs4 import BeautifulSoup
import csv
import sys

def scrape(url, output_file):
    try:
        page = requests.get(url)
        page.raise_for_status()
    except requests.RequestException as e:
        print(f"Chyba při stahování hlavní stránky: {e}")
        sys.exit(1)

    soup = BeautifulSoup(page.text, "html.parser")

    obce_nazvy = soup.find_all("td", class_="overflow_name")
    obce_kody_td = soup.find_all("td", class_="cislo")

    obce_kody = [td.text.strip() for td in obce_kody_td if td.find("a")]
    obce_nazvy = [td.text.strip() for td in obce_nazvy]

    if not obce_kody:
        print("Nebyla načtena žádná čísla obcí. Možná má stránka jinou strukturu?")
        sys.exit(1)

    data_radky = []
    vsechny_strany = set()

    for idx, kod_obce in enumerate(obce_kody):
        nazev_obce = obce_nazvy[idx] if idx < len(obce_nazvy) else f"Obec_{kod_obce}"
        print(f"📥 Zpracovávám: {kod_obce} - {nazev_obce}")

        odkaz_obec = f"https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec={kod_obce}&xvyber=7103"
        try:
            obec_resp = requests.get(odkaz_obec)
            obec_resp.raise_for_status()
        except requests.RequestException:
            print(f"Nelze načíst stránku pro obec {kod_obce}")
            continue

        obec_soup = BeautifulSoup(obec_resp.text, "html.parser")

        def najdi_text(headers):
            td = obec_soup.find("td", headers=headers)
            return td.text.replace('\xa0', '') if td else "0"

        volici = najdi_text("sa2")
        obalky = najdi_text("sa5")
        platne = najdi_text("sa6")

        strany = [td.text for td in obec_soup.find_all("td", class_="overflow_name")]
        hlasy_td = [td for td in obec_soup.find_all("td", class_="cislo") if td.has_attr("headers") and "t" in td["headers"] and "b3" in td["headers"]]
        hlasy = [td.text.replace('\xa0', '') for td in hlasy_td]

        data = {
            "Kód obce": kod_obce,
            "Název obce": nazev_obce,
            "Voliči v seznamu": volici,
            "Vydané obálky": obalky,
            "Platné hlasy": platne
        }

        for i in range(len(strany)):
            jmeno_strany = strany[i]
            hlasu = hlasy[i] if i < len(hlasy) else "0"
            data[jmeno_strany] = hlasu
            vsechny_strany.add(jmeno_strany)

        data_radky.append(data)

    hlavicka = ["Kód obce", "Název obce", "Voliči v seznamu", "Vydané obálky", "Platné hlasy"] + sorted(vsechny_strany)

    try:
        with open(output_file, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=hlavicka)
            writer.writeheader()
            for obec in data_radky:
                writer.writerow(obec)
        print(f"\n✅ CSV soubor byl úspěšně vytvořen: {output_file}")
    except Exception as e:
        print(f"❌ Chyba při zápisu CSV: {e}")


if __name__ == "__main__":
    DEFAULT_URL = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"
    DEFAULT_OUTPUT = "vysledky_prostejov.csv"

    if len(sys.argv) == 3:
        vstup_url = sys.argv[1]
        vystup_soubor = sys.argv[2]
    else:
        print("Argumenty nebyly zadány, používám výchozí hodnoty pro testování.")
        vstup_url = DEFAULT_URL
        vystup_soubor = DEFAULT_OUTPUT

    if not vystup_soubor.endswith(".csv"):
        vystup_soubor += ".csv"

    scrape(vstup_url, vystup_soubor)
