"""
Engeto_projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Martin Vopalecky
email: mvopale@email.cz
discord: martin_21315
"""
import requests
from bs4 import BeautifulSoup
import csv
import sys
import re

def vyhledej_obce_v_okrese(adresa):
    print("Pracuji...")
    response = requests.get(adresa)
    polivka = BeautifulSoup(response.text, 'html.parser')

    # najde prvky td ktera obsahuji cislo obce 
    cells = polivka.find_all('td', {'class': 'cislo'})
   
    # vyhleda odkazy na obce
    tabulka_obce_hodnoty = []
    for cell in cells:
        link = cell.find('a')
        obec = []
        obec.append("https://volby.cz/pls/ps2017nss/" + link['href'])
        obec.append(link.text)
        tabulka_obce_hodnoty.append(obec)

    return tabulka_obce_hodnoty

def vydoluj_obce(tabulka_obce_hodnoty):
 
    #vytvori zahlavi do csv
    response3 = requests.get(tabulka_obce_hodnoty[0][0])
    polivka = BeautifulSoup(response3.text, 'html.parser')
    strany_zahlavi = polivka.find_all('td', {'class': 'overflow_name'})
    zahlavi = ["kód obce","název obce","voliči v seznamu","vydané obálky","platné hlasy"]

    for strana in strany_zahlavi:
            zahlavi.append(strana.text)


    #prohledá jednotlivé odkazy na jednotlive obce a ziska data
    citac=0
    for polozka in tabulka_obce_hodnoty:

        citac +=1
        cisla_v_obci = []

        response2 = requests.get(polozka[0])
        polivka = BeautifulSoup(response2.text, 'html.parser')

        #najde nazev obce
        jmeno_obce = polivka.find('h3', string=re.compile("^\nObec")).text
        jmeno_obce=jmeno_obce[7:]
        jmeno_obce=jmeno_obce[0:-1]
        cisla_v_obci.append(jmeno_obce) 
        
        #vyhleda čísla za obec
        volici_v_seznamu = polivka.find('td',{'headers': 'sa2'})
        obalky = polivka.find('td',{'headers': 'sa3'})
        platne_hlasy = polivka.find('td',{'headers': 'sa6'})
        cisla_v_obci.append(volici_v_seznamu.text)
        cisla_v_obci.append(obalky.text)
        cisla_v_obci.append(platne_hlasy.text)

        #vyscrapuje hlasy za jednotlive strany v tabulce 1
        strany = polivka.find_all("td", {"headers":"t1sa2 t1sb3"})
        for strana in strany:
            cisla_v_obci.append(strana.text)
        #vyscrapuje hlasy za jednotlive strany v tabulce 2
        strany = polivka.find_all("td", {"headers":"t2sa2 t2sb3"})
        for strana in strany:
            cisla_v_obci.append(strana.text)     
            
        #prida hlasy stran za obec do celkove tabulky 
        for cislo in cisla_v_obci:
            tabulka_obce_hodnoty[citac-1].append(cislo)

    return(tabulka_obce_hodnoty,zahlavi)

def zapis_csv(tabulka_obce_hodnoty, zahlavi, csv_file):
    #vyjme odkaz na stranku obce z tabulky
    for radek in tabulka_obce_hodnoty:
            x=radek.pop(0)
        
    with open(csv_file, 'w', encoding="utf-8-sig", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(zahlavi)
        writer.writerows(tabulka_obce_hodnoty)
        print("Soubor .csv vytvořen")

def main():
    if len(sys.argv) != 3:
         print("Chyba, tento skript vyžaduje dva argumenty: URL a název výstupního souboru.")
         return

    adresa = sys.argv[1]
    csv_file = sys.argv[2]

    tabulka_obce_hodnoty = vyhledej_obce_v_okrese(adresa)
    tabulka_obce_hodnoty,zahlavi = vydoluj_obce(tabulka_obce_hodnoty)
    zapis_csv(tabulka_obce_hodnoty, zahlavi, csv_file)
    print("Konec programu")

if __name__ == "__main__":
    main()


