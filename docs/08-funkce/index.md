# Lekce 8 - Funkce

<div class="lesson-meta">
<strong>Doporučený čas:</strong> 60-75 minut<br>
<strong>Výstup lekce:</strong> Student zavolá vestavěné funkce, použije funkce objektů, vytvoří vlastní funkci a předá jí parametr.<br>
<strong>Zdrojová předloha:</strong> Python-first steps-p.51, strany 44-47, kapitola Functions
</div>

## Co se dnes naučíš

- zavolat funkci pomocí jejího jména a závorek
- předat funkci parametr
- použít vestavěné funkce `input()`, `print()`, `max()` a `min()`
- zavolat funkci přes tečku, například `.upper()`
- vytvořit vlastní funkci pomocí `def`
- použít `return` pro vrácení výsledku

## Proč to potřebujeme

Programátoři mají rádi zkratky, které usnadňují psaní kódu. Funkce je pojmenovaný blok kódu, který můžeš spustit opakovaně, aniž bys ho pokaždé psal znovu.

!!! info "Důležitá myšlenka"
    Funkci zavoláš jejím jménem a závorkami. Pokud funkce potřebuje data, vložíš je do závorek jako parametry.

## Slova, která se u funkcí používají

| Pojem | Význam |
| --- | --- |
| call | zavolat funkci |
| define | definovat funkci pomocí `def` |
| parameter | data předaná funkci |
| return value | hodnota, kterou funkce vrátí |

## Vestavěné funkce

Některé funkce už Python obsahuje. Ve skenu se připomínají například `input()` a `print()` a potom se ukazují funkce `max()` a `min()`.

```python title="code/01_builtin_functions.py" linenums="1"
name = input("What is your name? ")
greeting = "Hello " + name
print(greeting)

print(max(10, 16, 30, 21, 25, 28))
print(min(10, 16, 30, 21, 25, 28))
```

| Funkce | Co dělá |
| --- | --- |
| `input()` | načte text od uživatele |
| `print()` | zobrazí výsledek na obrazovce |
| `max(...)` | vybere největší hodnotu |
| `min(...)` | vybere nejmenší hodnotu |

## Jiný způsob volání

Některé hodnoty mají vlastní funkce. Volají se tak, že za hodnotu nebo proměnnou napíšeš tečku, název funkce a závorky.

```python title="code/02_string_functions.py" linenums="1"
print("bang".upper())

message = "Python makes me happy"
print(message.replace("happy", ":D"))

countdown = [1, 2, 3]
countdown.reverse()
print(countdown)
```

| Část programu | Význam |
| --- | --- |
| `"bang".upper()` | vrátí řetězec velkými písmeny |
| `message.replace("happy", ":D")` | nahradí část řetězce jiným textem |
| `countdown.reverse()` | otočí pořadí položek v seznamu |

## Vytvoření funkce

Na straně 46 se funkce vytvoří pomocí klíčového slova `def`. První funkce spočítá, kolik sekund je v jednom dni.

```python title="code/03_seconds_per_day.py" linenums="1"
def print_seconds_per_day():
    hours = 24
    minutes = hours * 60
    seconds = minutes * 60
    print(seconds)

print_seconds_per_day()
```

| Část programu | Význam |
| --- | --- |
| `def print_seconds_per_day():` | definuje novou funkci |
| odsazené řádky | tělo funkce |
| `print_seconds_per_day()` | zavolá funkci |

## Přidání parametru a návratové hodnoty

Když chceš funkci použít pro různý počet dní, předáš jí parametr `days`. Funkce potom vrátí výsledek pomocí `return`.

```python title="code/04_convert_days.py" linenums="1"
def convert_days_to_seconds(days):
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    return seconds

total_seconds = convert_days_to_seconds(7)
print(total_seconds)
```

## Zkus změnit

- U `max()` a `min()` změň čísla v závorkách.
- Zkus zavolat `.upper()` na jiný řetězec.
- Ve funkci `convert_days_to_seconds()` změň počet dní ze 7 na jiné číslo.
- Přejmenuj funkci tak, aby její název pořád jasně říkal, co dělá.

## Časté chyby

!!! warning "Častá chyba: Zapomeneš závorky při volání"
    **Proč vznikne:** Samotný název funkce nestačí ke spuštění.

    **Oprava:** Napiš například `print_seconds_per_day()`.

!!! warning "Častá chyba: Špatné odsazení těla funkce"
    **Proč vznikne:** Python podle odsazení pozná, které příkazy patří do funkce.

    **Oprava:** Všechny řádky uvnitř funkce odsaď stejně.

## Tahák

| Zápis | K čemu slouží |
| --- | --- |
| `function()` | volání funkce |
| `function(value)` | volání s parametrem |
| `text.upper()` | funkce volaná přes tečku |
| `def name():` | definice vlastní funkce |
| parametr | hodnota předaná funkci |
| `return` | vrácení výsledku |

## Co už umím

- [ ] umím zavolat funkci
- [ ] rozumím parametru
- [ ] umím použít `max()` a `min()`
- [ ] umím zavolat funkci přes tečku
- [ ] umím definovat vlastní funkci
- [ ] umím použít `return`

## Shrnutí

!!! success "Zapamatuj si"
    Funkce šetří opakování a dávají programu jména pro důležité kroky. Některé funkce jsou v Pythonu hotové, jiné si můžeš vytvořit pomocí `def`.
