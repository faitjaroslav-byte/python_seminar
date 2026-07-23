# Lekce 4 - Řetězce a seznamy

<div class="lesson-meta">
<strong>Doporučený čas:</strong> 60 minut<br>
<strong>Výstup lekce:</strong> Student uloží text do proměnné, spojí řetězce, zjistí délku řetězce a vytvoří seznam hodnot.<br>
<strong>Zdrojová předloha:</strong> Python-first steps-p.51, strany 26-27, části Working with strings a Lists
</div>

## Co se dnes naučíš

- vysvětlit řetězec jako posloupnost znaků
- uložit řetězec do proměnné
- spojit dva řetězce pomocí `+`
- použít funkci `len()`
- uložit více hodnot do seznamu
- vybrat položku ze seznamu podle pozice

## Proč to potřebujeme

Program často nepracuje jen s čísly. Potřebuje si pamatovat jména, zprávy, věty nebo celé sady hodnot. Přesně to řeší řetězce a seznamy na stranách 26-27.

!!! info "Důležitá myšlenka"
    Řetězec je posloupnost znaků. Seznam je uspořádaná sada položek. U seznamu Python počítá pozice od nuly.

## Práce s řetězci

Řetězec může být slovo, věta, jméno nebo libovolná zpráva. V Pythonu musí být začátek a konec řetězce označený uvozovkami.

### Řetězec v proměnné

```python title="code/01_strings.py" linenums="1"
name = "Ally Alien"
print(name)

greeting = "Welcome to Earth, "
message = greeting + name
print(message)

print(len(message))
```

| Část programu | Význam |
| --- | --- |
| `name = "Ally Alien"` | uloží řetězec do proměnné `name` |
| `print(name)` | vypíše uloženou hodnotu |
| `greeting + name` | spojí dva řetězce dohromady |
| `message` | uloží spojený řetězec |
| `len(message)` | spočítá počet znaků včetně mezer |

!!! tip "Délka řetězce"
    `len()` je vestavěná funkce. Počítá délku zprávy `Welcome to Earth, Ally Alien`, včetně mezer a čárky.

## Seznamy

Když potřebuješ uložit hodně dat najednou nebo zachovat jejich pořadí, použiješ seznam. Seznam je uložený v jedné proměnné a položky jsou zapsané v hranatých závorkách.

### Mnoho samostatných proměnných

Kdyby měl tým jen tři hráče, šlo by jména zapsat do tří proměnných.

```python
rockets_player_1 = "Rory"
rockets_player_2 = "Rav"
rockets_player_3 = "Rachel"
```

U šesti hráčů už je přehlednější použít seznam.

```python title="code/02_lists.py" linenums="1"
rockets_players = ["Rory", "Rav", "Rachel", "Renata", "Ryan", "Ruby"]
planets_players = ["Peter", "Pablo", "Polly", "Penny", "Paula", "Patrick"]

print(rockets_players[0])
print(planets_players[5])
```

| Část programu | Význam |
| --- | --- |
| `[...]` | hranaté závorky tvoří seznam |
| čárky | oddělují položky seznamu |
| `rockets_players[0]` | vybere první položku: `Rory` |
| `planets_players[5]` | vybere šestou položku: `Patrick` |

!!! warning "Pozice začínají nulou"
    První položka seznamu má pozici `0`. Proto je šestá položka na pozici `5`.

## Zkus změnit

- Změň jméno v proměnné `name`.
- Uprav text v proměnné `greeting` a sleduj změnu výsledné zprávy.
- Přidej další jméno do seznamu `rockets_players`.
- Vyber ze seznamu jinou položku a ověř, že počítáš od nuly.

## Časté chyby

!!! warning "Častá chyba: Chybí uvozovky u řetězce"
    **Proč vznikne:** Python pak chápe text jako název proměnné.

    **Oprava:** Text zapisuj do uvozovek, například `"Ally Alien"`.

!!! warning "Častá chyba: Špatný index seznamu"
    **Proč vznikne:** Python počítá od nuly, ne od jedničky.

    **Oprava:** Pro první položku použij `[0]`, pro druhou `[1]`.

## Tahák

| Zápis | K čemu slouží |
| --- | --- |
| `"Ally Alien"` | řetězec |
| `name = "Ally Alien"` | řetězec uložený v proměnné |
| `greeting + name` | spojení řetězců |
| `len(message)` | délka řetězce |
| `players = ["Rory", "Rav"]` | seznam |
| `players[0]` | první položka seznamu |

## Co už umím

- [ ] vím, co je řetězec
- [ ] umím spojit dva řetězce
- [ ] umím použít `len()`
- [ ] umím vytvořit seznam
- [ ] umím vybrat položku seznamu podle pozice

## Shrnutí

!!! success "Zapamatuj si"
    Řetězce ukládají text. Seznamy ukládají více hodnot najednou. U seznamů vždy počítej pozice od nuly.
