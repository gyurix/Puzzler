# Puzzler

## Installation

- Install all the dependencies from the `requirements.txt`
- Run the program

## Automatic testing

- Run `pytest -vv --durations=0 tests.py`
- My test results can be found at `testResults.txt`

## Task

Našou úlohou je nájsť riešenie 8-hlavolamu. Hlavolam je zložený z 8 očíslovaných políčok a jedného prázdneho miesta. Políčka je možné presúvať hore, dole, vľavo alebo vpravo, ale len ak je tým smerom medzera. Je vždy daná nejaká východisková a nejaká cieľová pozícia a je potrebné nájsť postupnosť krokov, ktoré vedú z jednej pozície do druhej.

Príkladom môže byť nasledovná začiatočná a koncová pozícia:

**Začiatok:**
```
1 	2 	3
4 	5 	6
7 	8
```
	 
**Koniec:**
```
1 	2 	3
4 	6 	8
7 	5
```
 	 
Im zodpovedajúca postupnosť krokov je:
- VPRAVO
- DOLE
- VĽAVO
- HORE.

## Implementácia
Keď chceme túto úlohu riešiť algoritmami prehľadávania stavového priestoru, musíme si konkretizovať niektoré pojmy:

### Stav
Stav predstavuje aktuálne rozloženie políčok. Počiatočný stav môžeme zapísať napríklad

`((1 2 3)(4 5 6)(7 8 m))` alebo `(1 2 3 4 5 6 7 8 m)`

Každý zápis má svoje výhody a nevýhody.
Prvý (vo všeobecnosti) umožňuje spracovať ľubovoľný hlavolam rozmerov `m*n`,
druhý má jednoduchšiu realizáciu operátorov.

Vstupom algoritmov sú práve dva stavy: začiatočný a cieľový.
Vstupom programu však môže byť aj ďalšia informácia, napríklad výber heuristiky.
 
### Operátory
**Operátory sú len štyri:**
- VPRAVO
- DOLE
- VLAVO
- HORE

Operátor má jednoduchú úlohu - dostane nejaký stav a ak je to možné,
vráti nový stav. Ak operátor na vstupný stav nie je možné použiť,
výstup nie je definovaný.

V konkrétnej implementácii je potrebné výstup buď vhodne dodefinovať,
alebo zabrániť volaniu nepoužiteľného operátora.

Všetky operátory pre tento problém majú rovnakú váhu.

#### Príklad použitia operátora DOLE:

**Vstup:** `((1 2 3)(4 5 6)(7 8 m))`

**Výstup:** `((1 2 3)(4 5 m)(7 8 6))`

### Heuristická funkcia
Niektoré z algoritmov potrebujú k svojej činnosti dodatočnú informáciu o riešenom probléme,
presnejšie odhad vzdialenosti od cieľového stavu.

Pre náš problém ich existuje niekoľko, môžeme použiť napríklad
- Počet políčok, ktoré nie sú na svojom mieste
- Súčet vzdialeností jednotlivých políčok od ich cieľovej pozície
- Kombinácia predchádzajúcich odhadov 

Tieto odhady majú navyše mierne odlišné vlastnosti podľa toho, či medzi políčka počítame alebo nepočítame aj medzeru.

#### Príklad

Heuristika č. 2, bez medzery, odhaduje vzdialenosť nasledujúcich dvoch stavov na

```
1 	2 	3
4 	5 	6
7 	8 	 
```

```    	 	
7 	8 	6
5 	4 	3
2 	  	1
```
    
`4 + 3 + 1 + 1 + 1 + 1 + 2 + 2 = **15**

### Uzol
Stav predstavuje nejaký bod v stavovom priestore.
My však od algoritmov požadujeme, aby nám ukázali cestu.
Preto musíme zo stavového priestoru vytvoriť graf.
Našťastie to nie je zložitá úloha.
Stavy jednoducho nahradíme uzlami.

#### Čo obsahuje typický uzol?

**Musí minimálne obsahovať:**
- Stav (to, čo uzol reprezentuje)
- Odkaz na predchodcu (pre nás zaujímavá hrana grafu, reprezentovaná čo najefektívnejšie) 

**Okrem toho môže obsahovať ďalšie informácie:**
- Posledne použitý operátor
- Predchádzajúce operátory
- Hĺbka uzla
- Cena prejdenej cesty
- Odhad ceny cesty do cieľa
- Iné vhodné informácie o uzle 

Uzol by však nemal obsahovať údaje, ktoré sú nadbytočné a príslušný algoritmus ich nepotrebuje. Pri zložitých úlohách sa generuje veľké množstvo uzlov a každý zbytočný bajt v uzle dokáže spotrebovať množstvo pamäti a znížiť rozsah prehľadávania algoritmu. Nedostatok informácií môže zase extrémne zvýšiť časové nároky algoritmu. Použité údaje zdôvodnite. 

### Algoritmus

Každé zadanie používa svoj algoritmus, ale algoritmy majú mnohé spoločné črty. Každý z nich potrebuje udržiavať informácie o uzloch, ktoré už kompletne spracoval a o uzloch, ktoré už vygeneroval, ale zatiaľ sa nedostali na spracovanie. Algoritmy majú tendenciu generovať množstvo stavov, ktoré už boli raz vygenerované. S týmto problémom je tiež potrebné sa vhodne vysporiadať, zvlášť u algoritmov, kde rovnaký stav neznamená rovnako dobrý uzol.

Činnosť nasledujúcich algoritmov sa dá z implementačného hľadiska opísať nasledujúcimi všeobecnými krokmi:

1. Vytvor počiatočný uzol a umiestni medzi vytvorené a zatiaľ nespracované uzly
2. Ak neexistuje žiadny vytvorený a zatiaľ nespracovaný uzol, skonči s neúspechom - riešenie neexistuje
3. Vyber najvhodnejší uzol z vytvorených a zatiaľ nespracovaných, označ ho aktuálny
4. Ak tento uzol predstavuje cieľový stav, skonči s úspechom - vypíš riešenie
5. Vytvor nasledovníkov aktuálneho uzla a zaraď ho medzi spracované uzly
6. Vytrieď nasledovníkov a ulož ich medzi vytvorené a zatiaľ nespracované
7. Choď na krok 2. 

Uvedené kroky sú len všeobecné a pre jednotlivé algoritmy ich treba ešte vždy rôzne upravovať
a optimalizovať. 

[Niekoľko výsledkov z prehľadávania do šírky v `M*N` hlavolame.](http://www2.fiit.stuba.sk/~kapustik/MN%20hlavolam.html) 