# Lekce 4 - Rozhodování

<div class="lesson-meta">
<strong>Doporučený čas:</strong> 75-90 minut<br>
<strong>Výstup lekce:</strong> Student použije porovnání, booleovské hodnoty a větvení `if`, `else` a `elif` podle ukázek z kapitoly Making decisions.<br>
</div>

## Co se dnes naučíš

- porovnat dvě hodnoty
- rozpoznat hodnoty `True` a `False`
- použít logické operátory `and` a `or`
- zapsat jednoduchou podmínku `if`
- přidat druhou větev podmínky pomocí `else`
- zapsat více větví podmínky pomocí `elif`

## Proč to potřebujeme

Každý den děláš rozhodnutí podle odpovědí na otázky: je venku tma, prší, mám dost let nebo jsem dost vysoký? Program se rozhoduje podobně. Nejprve porovná hodnoty a podle výsledku vykoná určitou část kódu.

!!! info "Důležitá myšlenka"
    Výsledek porovnání je booleovská hodnota: buď `True`, nebo `False`.

## Logické hodnoty (Boolean)

Počítač umí porovnávat hodnoty a rozhodovat, zda je nějaké tvrzení pravdivé. Výsledkem je vždy hodnota True nebo False, kterou můžeš uložit do proměnné nebo přímo vypsat.

### Kdo byl George Boole?

**George Boole (1815-1864)** byl anglický matematik, který vytvořil **Booleovu algebru** - matematiku pracující pouze se dvěma hodnotami: **PRAVDA (`True`)** a **NEPRAVDA (`False`)**. Díky jeho myšlenkám dnes mohou počítače rozhodovat, zda je nějaká podmínka splněna. V programování se s nimi setkáš například při použití operátorů **`and`**, **`or`** a **`not`**.

!!! tip "Zajímavost"
    Přestože George Boole žil dávno před vznikem počítačů, jeho práce tvoří jeden ze základů moderní informatiky a digitální techniky.

```python title="code/01_booleans.py" linenums="1"
answer_one = True
answer_two = False

print(answer_one)
print(answer_two)
```

| Hodnota | Význam |
| --- | --- |
| `True` | podmínka platí |
| `False` | podmínka neplatí |

## Operátory porovnání

Porovnání si ukážeme na věku a také na ananasech a zebrách.

```python title="code/02_comparisons.py" linenums="1"
age = 10
print(age == 10)
print(age < 10)

pineapples = 5
zebras = 2
print(pineapples > zebras)
print(zebras > pineapples)
print((pineapples == 3) and (zebras == 2))
print((pineapples == 3) or (zebras == 2))
```

| Operátor | Význam |
| --- | --- |
| `==` | rovná se |
| `!=` | nerovná se |
| `<` | menší než |
| `>` | větší než |
| `<=` | menší nebo rovno |
| `>=` | větší nebo rovno |

!!! warning "Jedno a dvě rovnítka"
    `=` přiřazuje hodnotu do proměnné. `==` porovnává dvě hodnoty.

## Jízda na horské dráze

Na ceduli v zábavním parku stojí, že na horskou dráhu mohou pouze lidé starší než 8 let a vyšší než 4 stopy a 7 palců. Mia je 10 let a měří 5 stop. 
Pomocí Python Shellu ověříme, zda může na horskou dráhu. Zadej následující řádky kódu, které vytvoří proměnné pro Miin věk a výšku a přiřadí jim správné hodnoty.
Poté zapiš pravidla pro vstup na horskou dráhu jako logický (Boolean) výraz a stiskni Enter.

```python title="code/03_rollercoaster.py" linenums="1"
age = 10
height = 60

if (age > 8) and (height > 55):
    print("You can go on the ride.")
```

Blok pod `if` se spustí jen tehdy, když jsou obě části podmínky pravdivé.

## Jedna větev, nebo druhá

Když program potřebuje udělat jednu věc při pravdivé podmínce a jinou věc při nepravdivé podmínce, použije `else`.

```python title="code/04_branches.py" linenums="1"
is_dark = input("Is it dark outside? y/n ")

if is_dark == "y":
    print("Goodnight! Zzzzzzzzz")
else:
    print("Coding time!")

tentacles = input("Do you have tentacles? y/n ")

if tentacles == "y":
    print("I never knew octopuses could type!")
else:
    print("Greetings, human!")
```

| Část programu | Význam |
| --- | --- |
| `input(...)` | načte odpověď uživatele |
| `if is_dark == "y":` | testuje, zda uživatel odpověděl `y` |
| odsazený blok | spustí se, když je podmínka pravdivá |
| `else:` | spustí se, když podmínka pravdivá není |

## Více větví

Když jsou možnosti více než dvě, použiješ `elif`. Sken ukazuje příklad s předpovědí počasí.

```python title="code/05_weather.py" linenums="1"
weather = input("What is the forecast for today? (rain/snow/sun) ")

if weather == "rain":
    print("Remember your umbrella!")
elif weather == "snow":
    print("Remember your woolly gloves!")
else:
    print("Remember your sunglasses!")
```

Python zkouší podmínky shora dolů. Jakmile najde první pravdivou větev, spustí její blok a ostatní větve přeskočí.

## Zkus změnit

- V příkladu s věkem změň hodnotu `age` a sleduj výsledek.
- Změň počet ananasů nebo zeber a znovu vyhodnoť porovnání.
- U horské dráhy nastav výšku pod 55 a vysvětli, proč se zpráva nevypíše.
- V příkladu s počasím přidej další možnost, například `wind`.

## Časté chyby

!!! warning "Častá chyba: `=` místo `==`"
    **Proč vznikne:** Jedno rovnítko ukládá hodnotu, dvě rovnítka porovnávají.

    **Oprava:** V podmínce piš například `age == 10`.

!!! warning "Častá chyba: Chybí dvojtečka"
    **Proč vznikne:** Řádek s `if`, `elif` nebo `else` otevírá blok.

    **Oprava:** Na konec řádku napiš `:`.

!!! warning "Častá chyba: Špatné odsazení"
    **Proč vznikne:** Python podle odsazení pozná, co patří do větve.

    **Oprava:** Příkazy uvnitř větve odsaď stejně.

## Tahák

| Zápis | K čemu slouží |
| --- | --- |
| `True` / `False` | pravda / nepravda |
| `==` | porovnání rovnosti |
| `and` | musí platit obě podmínky |
| `or` | stačí jedna pravdivá podmínka |
| `if podmínka:` | první větev |
| `else:` | větev pro ostatní případy |
| `elif podmínka:` | další testovaná možnost |

## Co už umím

- [ ] umím porovnat dvě hodnoty
- [ ] rozumím hodnotám `True` a `False`
- [ ] umím použít `and` a `or`
- [ ] umím zapsat `if`
- [ ] rozumím odsazení bloku
- [ ] umím použít `else` a `elif`

## Shrnutí

!!! success "Zapamatuj si"
    Rozhodování začíná otázkou, která má výsledek `True` nebo `False`. Podle výsledku Python spustí odpovídající odsazený blok.
