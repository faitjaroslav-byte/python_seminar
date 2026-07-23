# Lekce 5 - Cykly

<div class="lesson-meta">
<strong>Doporučený čas:</strong> 60-75 minut<br>
<strong>Výstup lekce:</strong> Student použije `for`, `while`, nekonečný cyklus a cyklus uvnitř cyklu podle ukázek z kapitoly Loopy loops.<br>
<strong>Zdrojová předloha:</strong> Python-first steps-p.51, strany 32-35, kapitola Loopy loops
</div>

## Co se dnes naučíš

- opakovat blok kódu pomocí `for`
- použít `range()` pro počet opakování
- opakovat kód pomocí `while`
- zastavit cyklus podle odpovědi uživatele
- rozpoznat nekonečný cyklus
- vložit jeden cyklus dovnitř druhého

## Proč to potřebujeme

Počítače jsou dobré v nudné opakované práci. Místo abys psal stejný řádek desetkrát, necháš Python zopakovat blok kódu za tebe.

!!! info "Důležitá myšlenka"
    Tělo cyklu je odsazený blok příkazů. Všechny příkazy v těle cyklu se opakují.

## For loops

Když víš, kolikrát se má blok kódu opakovat, použij `for`. Emma nechce, aby někdo lezl do jejího pokoje, takže program vypíše stejnou zprávu desetkrát.

```python title="code/01_for_loop.py" linenums="1"
for counter in range(1, 11):
    print("Emma's Room - Keep Out!!!")
```

| Část programu | Význam |
| --- | --- |
| `counter` | proměnná cyklu, která sleduje pořadí opakování |
| `range(1, 11)` | vytvoří hodnoty od 1 do 10 |
| odsazení o čtyři mezery | označuje tělo cyklu |
| `print(...)` | řádek, který se opakuje |

!!! tip "Range"
    `range(1, 11)` znamená čísla 1 až 10. Poslední hranice není zahrnutá.

## While loops

Když nevíš předem, kolikrát se má cyklus opakovat, použij `while`. Ahmed počítá, kolik hrochů už balancuje na sobě, a vždy se zeptá, jestli má přidat dalšího.

```python title="code/02_while_hippos.py" linenums="1"
hippos = 0
answer = "y"

while answer == "y":
    hippos = hippos + 1
    print(str(hippos) + " balancing hippos!")
    answer = input("Add another hippo? (y/n) ")
```

| Část programu | Význam |
| --- | --- |
| `hippos = 0` | počítadlo hrochů |
| `answer = "y"` | počáteční odpověď, aby cyklus poprvé běžel |
| `while answer == "y":` | cyklus běží, dokud je odpověď `y` |
| `hippos = hippos + 1` | přidá dalšího hrocha |
| `str(hippos)` | převede číslo na text, aby šlo spojit se zprávou |

## Nekonečné cykly

Někdy chceš, aby program běžel pořád. Ukážeme si to na cyklu, který nikdy nemá nepravdivou podmínku.

```python title="code/03_infinite_loop.py" linenums="1"
while True:
    print("This is an infinite loop!")
```

!!! warning "Zastavení cyklu"
    Nekonečný cyklus můžeš zastavit například přes `Ctrl-C`, zavřením okna nebo tlačítkem Stop podle prostředí, ve kterém program běží.

## Cyklus uvnitř cyklu

Jeden cyklus může být uvnitř druhého. Vnější cyklus opakuje celé tělo, vnitřní cyklus se spustí pokaždé znovu.

```python title="code/04_nested_loop.py" linenums="1"
for hooray_counter in range(1, 4):
    for hip_counter in range(1, 3):
        print("Hip")
    print("Hooray!")
```

Tento program vypíše dvakrát `Hip` a potom `Hooray!`. Celý vzor zopakuje třikrát.

## Zkus změnit

- V prvním příkladu změň počet opakování na 5.
- U hrochů zadej několikrát `y` a potom `n`.
- U nekonečného cyklu si před spuštěním připomeň, jak ho zastavíš.
- Vnořený cyklus uprav tak, aby vypisoval třikrát `Hip`.

## Časté chyby

!!! warning "Častá chyba: Špatné odsazení těla cyklu"
    **Proč vznikne:** Python podle odsazení pozná, které příkazy patří do cyklu.

    **Oprava:** Řádky v těle cyklu odsaď stejně.

!!! warning "Častá chyba: Nekonečný cyklus omylem"
    **Proč vznikne:** Podmínka se nikdy nezmění na `False`.

    **Oprava:** U `while` zkontroluj, že se hodnota použitá v podmínce uvnitř cyklu mění.

## Tahák

| Zápis | K čemu slouží |
| --- | --- |
| `for counter in range(1, 11):` | opakování známý počet krát |
| `while answer == "y":` | opakování podle podmínky |
| `while True:` | nekonečný cyklus |
| `str(number)` | převod čísla na řetězec |
| vnořený cyklus | cyklus zapsaný uvnitř jiného cyklu |

## Co už umím

- [ ] umím použít `for` s `range()`
- [ ] rozumím tělu cyklu a odsazení
- [ ] umím použít `while`
- [ ] vím, jak vznikne nekonečný cyklus
- [ ] poznám cyklus uvnitř cyklu

## Shrnutí

!!! success "Zapamatuj si"
    `for` se hodí, když znáš počet opakování. `while` se hodí, když cyklus závisí na podmínce. V obou případech Python opakuje odsazené tělo cyklu.
