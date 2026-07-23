# Lekce 5 - Cykly

<div class="lesson-meta">
<strong>Doporučený čas:</strong> 60-75 minut<br>
<strong>Výstup lekce:</strong> Student použije `for`, `while`, nekonečný cyklus a cyklus uvnitř cyklu podle ukázek z kapitoly Loopy loops.<br>
</div>

## Co se dnes naučíš

- použít cyklus `for` k opakování bloku kódu
- použít funkci `range()` k určení počtu opakování
- vytvořit cyklus `while` řízený podmínkou
- ukončit cyklus podle odpovědi uživatele
- rozpoznat a opravit nekonečný cyklus
- vložit jeden cyklus dovnitř druhého (vnořené cykly)


## Proč to potřebujeme

Počítače jsou skvělé v opakování stále stejných úkolů. Místo psaní stejného kódu znovu a znovu můžeš nechat Python, aby celý blok kódu opakoval za tebe.

!!! info "Důležitá myšlenka"
    Tělo cyklu je odsazený blok příkazů. Všechny příkazy v těle cyklu se opakují.

## for cyklus

Když víš, kolikrát se má blok kódu opakovat, použij cyklus `for`. 

Emma nechce, aby někdo lezl do jejího pokoje, takže program vypíše stejnou zprávu desetkrát.

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

## Cyklus while 

Když nevíš předem, kolikrát se má cyklus opakovat, použij `while`. 

Ahmed počítá, kolik hrochů už balancuje na sobě, a vždy se zeptá, jestli má přidat dalšího.

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

Někdy potřebujeme, aby program běžel nepřetržitě. Toho dosáhneme cyklem, jehož podmínka je vždy pravdivá. Takový cyklus se nikdy sám neukončí.

```python title="code/03_infinite_loop.py" linenums="1"
while True:
    print("This is an infinite loop!")
```

!!! warning "Zastavení cyklu"
    Nekonečný cyklus můžeš zastavit například přes `Ctrl-C`, zavřením okna nebo tlačítkem Stop podle prostředí, ve kterém program běží.

## Cyklus uvnitř cyklu

Jeden cyklus může obsahovat další cyklus. Při každém průchodu vnějšího cyklu se vnitřní cyklus spustí znovu od začátku.

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
| `for counter in range(1, 11):` | opakuje blok kódu 10x |
| `while answer == "y":` | opakuje blok kódu dokud platí podmínka |
| `while True:` | vytváří (nekonečný) cyklus |
| `str(number)` | převod čísla na řetězec |
| vnořený cyklus | cyklus umístěný uvnitř jiného cyklu |

## Co už umím

- [ ] umím použít cyklus `for` s počtem opakování `range()`
- [ ] rozumím tělu cyklu a odsazení
- [ ] umím použít podmíněný cyklus `while`
- [ ] vím, jak vznikne nekonečný cyklus a jak ho ukončit
- [ ] poznám cyklus uvnitř cyklu

## Shrnutí

!!! success "Zapamatuj si"
    `for` se hodí, když předem víš kolikrát se má kód opakovat. `while` použij když opakování závisí na splnění podmínky. V obou případech Python opakuje blok kódu se stejným odsazením.
