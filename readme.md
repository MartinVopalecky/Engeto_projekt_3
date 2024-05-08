Engeto projekt 3
=============
---
Třetí projekt pro získání certifikátu u Engeta

----

## Popis projektu
Tento projekt slouží k získání výsledků z parlamentních voleb 2017.

## Instalace knihoven
Knihovny které jsou použity v kódu jsou uložené v souboru requirements.txt.  
Je možné je naistalovat pomocí příkazu do nového virtuálního prostředí: 

``` pip install -r requirements.txt ```

## Spuštění knihoven

``` python  Engeto_projekt_3 <odkaz uzemniho celku> <vysledny soubor>   ```

Výsledky se uloží v souboru .csv

## Ukázka projektu
Výsledky hlasování pro okres Plzeň

1.argument: ```https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=4&xnumnuts=3203```  
2.argument: ```    vysledky_plzen.csv                   ```

Spuštění programu:
``` python Engeto_projekt_3.py  "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=4&xnumnuts=3203"  vysledky_plzen.csv           ```

Ukázka části výstupu:
```  
kód obce,název obce,voliči v seznamu,vydané obálky,platné hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,OBČANÉ 2011-SPRAVEDL. PRO LIDI,Referendum o Evropské unii,TOP 09,ANO 2011,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
558851,Dýšina,1 349,860,853,114,0,0,48,0,52,41,10,5,16,1,2,119,0,3,45,269,5,34,0,3,2,1,80,3,-
558966,Chrást,1 429,1 002,999,151,1,1,51,1,31,63,8,4,15,1,2,111,1,1,45,354,1,24,0,11,5,2,114,1,-
557846,Chválenice,561,369,369,50,3,0,21,0,13,21,7,7,7,1,1,52,0,0,38,104,0,8,0,3,2,0,29,2,-
559130,Kyšice,734,508,506,87,1,0,39,0,23,32,5,3,12,0,0,52,2,0,22,153,0,24,0,8,2,1,38,2,-
540561,Letkov,510,410,409,74,0,0,21,0,16,19,6,2,6,2,6,41,0,0,34,126,0,15,0,3,0,0,37,1,-

 ```

         



