# PROJECT STANDARD

**Moderní učebnice Pythonu**

*Verze 1.0 – rozšířené zadání, autorská pravidla a Definition of Done pro Codex*


| Hlavní záměr | Vytvořit profesionální online učebnici Pythonu pro studenty středních škol. Učebnice bude moderně zpracovaná v MkDocs Material, ale její didaktická struktura se musí přísně řídit předanými PDF materiály. |
| --- | --- |


| Závazné PDF předlohy | Učebnice bude vytvořena podle PDF Python_first_steps-p.51 a Python_52-107. Tyto dokumenty jsou závaznou předlohou pro pořadí výuky, strukturu lekcí, návaznost projektů a zavádění nových příkazů. |
| --- | --- |


| Použití ukázkové lekce | Soubor lekce-02-prvni-program(1).md slouží jako stylová inspirace pro výsledný vzhled lekce: metadata, cíle, boxy, tabulky, checklist, tahák a přehledné vedení studenta. Nesmí však měnit závaznou strukturu PDF předloh. |
| --- | --- |


## Obsah dokumentu

- 1. Účel a rozsah projektu
- 2. Závazné zdrojové materiály
- 3. Princip věrnosti předloze
- 4. Charakter výsledné učebnice
- 5. Role ukázkové lekce
- 6. Lesson Authoring Guide
- 7. Šablona lekce v Markdownu
- 8. Visual Style Guide
- 9. Flowchart Standard
- 10. SVG a ilustrace
- 11. Repository & Markdown Convention
- 12. Python Code Convention
- 13. Práce s projekty
- 14. AI / Codex pravidla
- 15. Definition of Done
- 16. Kontrolní checklisty
- 17. Doporučený workflow pro Codex
- 18. Doporučené prompty pro Codex
- 19. Shrnutí hlavního principu


## 1. Účel a rozsah projektu

Cílem je vytvořit moderní, vizuálně kvalitní a dlouhodobě udržovatelnou učebnici Pythonu pro studenty středních škol, přibližně ve věku 17–19 let. Výstupem bude webová učebnice publikovaná pomocí MkDocs Material a spravovaná v GitHub repozitáři.
Učebnice nemá být referenční příručka ani dokumentace jazyka Python. Má studenta vést krok za krokem: od motivace přes ukázku, rozbor, schéma, úpravy programu až po procvičení a projekt.

| Klíčový požadavek | Moderní zpracování nesmí znamenat změnu didaktické koncepce. Nová verze má být vizuálně a technologicky modernější, ale výukově věrná předloze. |
| --- | --- |


## 2. Závazné zdrojové materiály

Veškerý obsah bude vycházet z těchto PDF dokumentů:
- Python_first_steps-p.51
- Python_52-107
Tyto soubory jsou považovány za závaznou osnovu. Codex ani jiný AI nástroj nesmí svévolně navrhovat nové pořadí témat, nové projekty nebo alternativní výukovou cestu.

| PDF materiál | Použití v projektu |
| --- | --- |
| Python_first_steps-p.51 | První část učebnice. Slouží jako zdroj struktury, pořadí lekcí, úvodních projektů a prvních programátorských pojmů. |
| Python_52-107 | Navazující část učebnice. Slouží jako zdroj dalších lekcí, projektů a postupného rozšiřování znalostí. |


## 3. Princip věrnosti předloze

Tento projekt není tvorbou nového kurzu Pythonu. Je to modernizace a přepracování předané učební předlohy do webové podoby. Věrnost předloze má přednost před kreativními návrhy AI.

| Zachovat | Přepracovat |
| --- | --- |
| Pořadí výuky | Jazyk textu a formulace |
| Strukturu lekcí | Grafické zpracování |
| Logiku projektů | SVG ilustrace a flowcharty |
| Postupné zavádění příkazů | Typografii a webovou prezentaci |
| Obtížnost a návaznost | Formátování v MkDocs Material |


| Zakázané chování AI | AI nesmí zaměnit učebnici za dokumentaci typu „syntax – příklad – cvičení“. Lekce musí zůstat učebnicové, vedené a didakticky postupné. |
| --- | --- |


## 4. Charakter výsledné učebnice

Výsledná učebnice má působit jako profesionálně vydaná publikace. Student by měl při čtení cítit jasné vedení: co se právě učí, proč to potřebuje, jak příkaz funguje, jak ho použije a na co si má dát pozor.
- Krátké a srozumitelné odstavce.
- Průběžné otázky a malé experimenty.
- Ukázky kódu s vysvětlením.
- Vizuální schémata a flowcharty.
- Boxy Tip, Pozor, Častá chyba, Zajímavost, Projekt.
- Kontrolní checklist na konci lekce.

## 5. Role ukázkové lekce

Ukázková lekce „Lekce 2 — První program v Pythonu“ se použije jako inspirace pro vizuální a formální styl. Zachovat přehlednost, metadata lekce, cíle, boxy, tabulky, checklist a tahák. Zároveň platí, že ukázka neurčuje pořadí výuky; to určují výhradně PDF předlohy.

| Prvek z ukázky | Použití v učebnici |
| --- | --- |
| lesson-meta blok | Používat pro čas, výstup lekce a případně předpoklady. |
| Co se dnes naučíš | Používat jako jasný úvodní přehled výstupů lekce. |
| Admonitions | Používat pro tipy, chyby, důležité myšlenky a projekty. |
| Tabulky rozboru kódu | Používat tam, kde pomáhají vysvětlit syntaxi nebo části programu. |
| Checklist „Co už umím“ | Používat na konci lekcí pro sebehodnocení studenta. |
| Tahák | Používat tam, kde dává smysl shrnout novou syntaxi. |


## 6. Lesson Authoring Guide

Codex musí při tvorbě každé lekce nejprve analyzovat odpovídající část PDF a až poté generovat Markdown, SVG a zdrojové soubory.

### 6.1 Doporučená struktura lekce

Přesná struktura se vždy řídí předlohou. Pokud předloha obsahuje následující části, musí být zachovány:
1. Název lekce a metadata: doporučený čas, cíl, výstup.
2. Krátká motivace: proč se téma učíme.
3. Nový pojem nebo příkaz.
4. Malý ukázkový program.
5. Rozbor programu řádek po řádku.
6. Logické schéma nebo flowchart.
7. Malé experimenty typu „zkus změnit…“.
8. Časté chyby a jejich oprava.
9. Projekt nebo větší úloha dle PDF.
10. Shrnutí a checklist.
11. Procvičení.

### 6.2 Povinný postup při tvorbě lekce

1. Najít odpovídající část v PDF Python_first_steps-p.51 nebo Python_52-107.
2. Zapsat stručnou analýzu: co je cílem lekce, jaké nové pojmy zavádí a jak navazuje na předchozí látku.
3. Opsat pouze strukturu, nikoliv text. Texty vytvořit nově vlastními slovy.
4. Zachovat pořadí příkladů a projektů.
5. Připravit všechny .py soubory do složky code/.
6. Překreslit potřebná schémata a obrázky jako SVG do složky images/.
7. Vytvořit index.md v učebnicovém stylu.
8. Ověřit, že lekce neobsahuje nový projekt ani přesunutou látku.

## 7. Šablona lekce v Markdownu

Následující šablona ukazuje formální strukturu. Obsah a pořadí částí se vždy přizpůsobí PDF předloze.

```markdown
# Lekce X — Název lekce

<div class="lesson-meta">
<strong>Doporučený čas:</strong> 45–60 minut<br>
<strong>Výstup lekce:</strong> Jednou větou popiš praktický výstup.
</div>

## Co se dnes naučíš

- výstup 1
- výstup 2
- výstup 3

## Proč to potřebujeme

Krátká motivace podle logiky PDF předlohy.

!!! info "Důležitá myšlenka"
    Jedna klíčová myšlenka lekce.

## Analýza problému

Zadání, vstupy, výstupy a jednoduchý algoritmus.

## Ukázkový program

```python title="code/01_ukazka.py" linenums="1"
# vložená nebo odkazovaná ukázka
```

## Rozbor programu

Tabulka nebo odstavce vysvětlující podstatné řádky.

## Schéma průběhu

![Popis schématu](images/schema.svg)

## Projekt / Procvičení

Pouze podle PDF předlohy.

## Co už umím

- [ ] bod 1
- [ ] bod 2

## Shrnutí

Krátké zopakování.
```


## 8. Visual Style Guide

Vizuální styl musí být jednotný napříč celou učebnicí. Student nesmí mít pocit, že každá kapitola vznikla jiným stylem.

| Typ prvku | Doporučený styl |
| --- | --- |
| Tip | Krátký praktický postřeh, který studentovi pomůže pracovat efektivněji. |
| Pozor | Varování před častým omylem nebo záměnou. |
| Častá chyba | Konkrétní chyba v kódu, vysvětlení příčiny a oprava. |
| Zajímavost | Doplňující souvislost, která není nutná pro splnění úlohy. |
| Projekt | Větší úloha nebo praktický výstup lekce. |
| Shrnutí | Krátké zopakování hlavních bodů. |


### 8.1 Doporučené ikony a boxy


| Účel | Ikona / název | Použití |
| --- | --- | --- |
| Cíl | Cíl lekce | Na začátku lekce. |
| Tip | Tip | Praktické doporučení. |
| Varování | Pozor | Rizikové místo nebo častý omyl. |
| Debug | Častá chyba | Chyba, výpis, oprava. |
| Projekt | Projekt | Větší úloha dle PDF. |
| Shrnutí | Zapamatuj si | Závěrečné shrnutí. |


## 9. Flowchart Standard

Flowcharty jsou důležitou součástí učebnice. Umožňují studentům vidět logiku programu dříve, než se soustředí na syntaxi Pythonu.

| Symbol | Význam | Použití |
| --- | --- | --- |
| Zaoblený obdélník | Start / Konec | Začátek a konec algoritmu. |
| Obdélník | Proces | Výpočet, přiřazení, běžný krok. |
| Rovnoběžník | Vstup / výstup | input(), print(), čtení nebo zobrazení hodnoty. |
| Kosočtverec | Rozhodnutí | Podmínka if / elif / else. |
| Šipka | Tok programu | Směr vykonávání kroků. |

- Všechna schémata ukládat jako SVG.
- Používat jednotnou tloušťku čar a stejný font.
- Nepoužívat screenshoty ani rastrové obrázky, pokud to není nezbytné.
- Schéma má být didaktické, ne pouze dekorativní.

## 10. SVG a ilustrace

Všechny obrázky budou vytvořeny nově. Cílem není kopírovat původní grafiku, ale zachovat její didaktickou funkci.

| Prvek | Pravidlo |
| --- | --- |
| Formát | Preferovat SVG. |
| Styl | Ploché čisté tvary, jednotné barvy, čitelné popisky. |
| Text ve schématu | Krátký, český, jednoznačný. |
| Velikost | Navrhovat tak, aby bylo čitelné na monitoru i projektoru. |
| Alternativní text | Každý obrázek musí mít popisný alt text v Markdownu. |


## 11. Repository & Markdown Convention

Repozitář bude organizován tak, aby byl přehledný pro učitele, studenty i Codex.

```text
docs/
  02_prvni_program/
    index.md
    code/
      01_hello.py
      02_poradi.py
    images/
      program-flow.svg
mkdocs.yml
README.md
requirements.txt
```

- Každá lekce má vlastní složku.
- Obsah lekce je v index.md.
- Zdrojové kódy jsou ve složce code/.
- Obrázky a schémata jsou ve složce images/.
- Nepoužívat mezery v názvech souborů.
- Používat malá písmena, čísla, pomlčky nebo podtržítka.

### 11.1 Markdown pravidla

- Používat nadpisy H1 až H3 konzistentně.
- Krátké odstavce, maximálně několik vět.
- Kód vkládat s názvem souboru, pokud jde o ukázku programu.
- Tabulky používat hlavně pro rozbor syntaxe nebo porovnání.
- Admonitions používat účelně, ne jako dekoraci.

## 12. Python Code Convention

Kód musí být jednoduchý, čitelný a odpovídat úrovni lekce. Nepoužívat konstrukce, které ještě nebyly podle PDF zavedeny.
- Každý program uložit jako samostatný .py soubor.
- Komentáře psát pouze tam, kde pomáhají pochopit záměr.
- Nepoužívat zbytečně pokročilé konstrukce.
- Programy musí být spustitelné samostatně.
- Ukázky musí odpovídat přesně tomu, co je vysvětleno v lekci.
- Názvy souborů číslovat podle pořadí v lekci.

| Typ souboru | Příklad názvu |
| --- | --- |
| První ukázka | 01_hello.py |
| Pořadí příkazů | 02_poradi.py |
| Projekt | project_animal_quiz.py |
| Oprava chyby | debug_syntax_error.py |


## 13. Práce s projekty

Projekty jsou pevnou součástí PDF předloh a mají zůstat zachovány. AI nesmí přidávat vlastní projekty jen proto, že by byly zajímavé nebo modernější.
1. Převzít projekt z odpovídající části PDF.
2. Zpracovat analýzu: co má program dělat, jaké vstupy a výstupy má, jaké kroky algoritmus obsahuje.
3. Nakreslit flowchart.
4. Vytvořit první verzi kódu odpovídající aktuálně známé látce.
5. Vysvětlit kód v učebnicovém stylu.
6. Přidat pouze taková rozšíření, která odpovídají předloze nebo jsou výslovně schválena.

| Požadavek na analýzu projektu | Každý projekt musí mít před kódem část „Analýza“. Student má nejprve chápat problém a algoritmus, teprve potom syntaxi. |
| --- | --- |


## 14. AI / Codex pravidla

Codex je implementační nástroj, ne autor nové didaktické koncepce. Při každém úkolu musí pracovat podle PDF a podle tohoto standardu.

| Codex smí | Codex nesmí |
| --- | --- |
| Přepsat text vlastními slovy | Změnit pořadí výuky |
| Vytvořit Markdown | Přidat nový projekt bez zadání |
| Vytvořit SVG schéma | Přeskočit analýzu projektu |
| Vytvořit .py soubory | Použít konstrukci, která nebyla zavedena |
| Opravit konzistenci | Sloučit nebo rozdělit lekce bez opory v PDF |


| Povinná instrukce pro Codex | Před každou změnou lekce nejprve porovnej výstup s odpovídající částí PDF Python_first_steps-p.51 nebo Python_52-107. Zachovej její strukturu a logiku. Teprve poté proveď moderní zpracování v Markdownu, SVG a Python souborech. |
| --- | --- |


## 15. Definition of Done

Lekce je dokončena pouze tehdy, když splňuje všechny následující body:
- Je ověřena proti odpovídající části PDF.
- Zachovává strukturu a pořadí předlohy.
- Text je nový, vlastními slovy.
- Všechny kódy jsou v samostatných .py souborech.
- Všechny obrázky a flowcharty jsou nové SVG.
- Markdown je kompatibilní s MkDocs Material.
- Lekce obsahuje cíle, vysvětlení, ukázky, procvičení a shrnutí podle předlohy.
- Kód je spustitelný a odpovídá úrovni dosud probrané látky.
- Neobsahuje nové projekty ani přesunutou látku bez zadání.
- Vizuální styl odpovídá ukázkové lekci a celkovému design systému.

## 16. Kontrolní checklisty


### 16.1 Checklist před tvorbou lekce

- Mám otevřenou odpovídající část PDF.
- Vím, které pojmy se v lekci nově zavádějí.
- Vím, jak lekce navazuje na předchozí část.
- Vím, které projekty nebo úlohy se mají zachovat.

### 16.2 Checklist před commitem

- Všechny odkazy v Markdownu fungují.
- Všechny .py soubory jsou ve správné složce.
- Všechny SVG soubory jsou ve složce images/.
- Navigace v mkdocs.yml odpovídá nové lekci.
- Kód neobsahuje neprobrané konstrukce.
- Lekce dodržuje strukturu PDF.

## 17. Doporučený workflow pro Codex

1. Vytvoř branch pro konkrétní lekci nebo sadu změn.
2. Najdi odpovídající část PDF.
3. Vytvoř krátký plán změn a seznam souborů.
4. Nejprve vytvoř nebo aktualizuj Markdown strukturu.
5. Poté vytvoř .py soubory.
6. Poté vytvoř SVG obrázky a flowcharty.
7. Zkontroluj odkazy, názvy souborů a navigaci v mkdocs.yml.
8. Spusť kontrolu Python souborů.
9. Spusť lokální build MkDocs, pokud je dostupný.
10. Commitni změny s jasnou commit message.

## 18. Doporučené prompty pro Codex

Následující prompty lze používat při práci nad jednotlivými lekcemi.

| Situace | Prompt |
| --- | --- |
| Analýza lekce | Analyzuj odpovídající část PDF a vypiš strukturu lekce, nové pojmy, příklady, projekty a schémata. Nic zatím negeneruj. |
| Tvorba lekce | Vytvoř Markdown lekci podle struktury PDF. Zachovej pořadí a logiku předlohy. Text přepiš vlastními slovy a použij styl ukázkové lekce. |
| Flowchart | Překresli schéma z PDF jako nové SVG. Zachovej didaktickou funkci, ale vytvoř vlastní moderní grafiku. |
| Kód | Vytvoř samostatné .py soubory odpovídající ukázkám v lekci. Nepoužívej konstrukce, které ještě nebyly zavedeny. |
| Kontrola | Zkontroluj lekci proti Project Standardu a vypiš, co případně nesplňuje Definition of Done. |


## 19. Shrnutí hlavního principu


| Projektová věta | Tato učebnice není novým kurzem Pythonu. Je to moderní, vizuálně kvalitnější a technologicky současná verze předaných PDF Python_first_steps-p.51 a Python_52-107. Zachovává jejich didaktickou strukturu, pořadí výuky a projekty, ale přepisuje texty vlastními slovy, vytváří novou grafiku v SVG a publikuje vše jako profesionální web pomocí MkDocs Material. |
| --- | --- |
