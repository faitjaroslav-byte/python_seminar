# Lekce 3 - Proměnné a vstup

<div class="lesson-meta">
<strong>Doporučený čas:</strong> 60 minut<br>
<strong>Výstup lekce:</strong> Student ulozi hodnotu do proměnné, načte text od uživatele a použije ho ve výstupu.<br>
<strong>Zdrojová předloha:</strong> Python-first steps-p.51, část Variables
</div>

## Co se dnes naučíš

- vysvětlit proměnnou jako pojménovane místo pro hodnotu
- použít input()
- spojit pevny text s hodnotou proměnné
- převést textovy vstup na číslo pomocí int()

## Proč to potřebujeme

Programy v PDF postupne prestavaji jen výpisovat hotovy text. Zacnou si pamatovat jméno hráče nebo odpověď uživatele.

!!! info "Důležitá myšlenka"
    Promenna ma jméno a hodnotu. Hodnota se muze v programu použít pozdeji, treba ve výpisu nebo vypoctu.

## Analýza problému

- vstupem je jméno a vek uživatele
- jméno zustava text
- vek se prevadi na číslo
- vystup použije ulozene hodnoty

## Schéma průběhu

![Lekce 3 - Proměnné a vstup - schéma průběhu](images/flowchart.svg){ .flowchart }

## Ukázkový program

```python title="code/vstup.py" linenums="1"
name = input("Jak se jmenujes? ")
age = int(input("Kolik ti je let? "))
print("Ahoj", name)
print("Za rok ti bude", age + 1)
```

[Stáhnout soubor `vstup.py`](code/vstup.py){ .md-button .md-button--primary }

## Rozbor programu

| Část programu | Význam |
| --- | --- |
| `name = input(...)` | načte odpověď a ulozi ji do proměnné |
| `int(input(...))` | převede odpověď na cele číslo |
| `age + 1` | použije číselnou hodnotu ve vypoctu |

## Zkus změnit

- Změň otazku pro vstup jmena.
- Zkus zadat místo veku slovo a sleduj chybovou hlášku.
- Doplň výpis, ktery použije jméno dvakrat.

## Časté chyby

!!! warning "Častá chyba: Zapomenuty prevod `int()`"
    **Proč vznikne:** Vek zustane text a nelze k nemu normalne pricist číslo.

    **Oprava:** Použij `int(input(...))` tam, kde cekas číslo.

!!! warning "Častá chyba: Mezera ve jmenu proměnné"
    **Proč vznikne:** Nazev proměnné nesmi obsahovat mezeru.

    **Oprava:** Použij napr. `user_name`.

## Tahák

| Zápis | K čemu slouží |
| --- | --- |
| `name = hodnota` | uložení hodnoty |
| `input("otázka")` | vstup od uživatele |
| `int(...)` | prevod na cele číslo |

## Co už umím

- [ ] umím vytvořít proměnnou
- [ ] umím načíst odpověď uživatele
- [ ] vím, ze input() vraci text
- [ ] umím převést vstup na číslo

## Shrnutí

!!! success "Zapamatuj si"
    Proměnné davaji programu pamet. Diky input() muze stejny program reagovat na ruzne uživatele.
