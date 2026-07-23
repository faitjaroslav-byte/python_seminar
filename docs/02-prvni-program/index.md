# Lekce 2 - První program

<div class="lesson-meta">
<strong>Doporučený čas:</strong> 45-60 minut<br>
<strong>Výstup lekce:</strong> Student vytvoří soubor ve VS Code, spustí první program, opraví jednoduchou chybu a rozšíří program o otázku na jméno.
</div>

## Co se dnes naučíš

- otevřít editor VS Code a založit nový soubor
- napsat první řádek programu
- uložit soubor s příponou `.py`
- spustit program a zkontrolovat výstup v terminálu
- opravit drobnou chybu v zápisu
- přidat další řádky, které se uživatele zeptají na jméno

## Proč to potřebujeme

První program má studentům ukázat celý postup práce: otevřít editor, napsat kód, uložit soubor, spustit program a zkontrolovat výsledek. Teprve potom má smysl program dále rozšiřovat.

!!! info "Důležitá myšlenka"
    Kód píšeš v editoru, ale výsledek uvidíš v terminálu. Když změníš program, musíš ho před dalším spuštěním znovu uložit.

## Jak bude program fungovat

Ve skenu je program vysvětlený jako krátký postup:

1. program vypíše pozdrav,
2. zeptá se uživatele na jméno,
3. uživatel jméno napíše,
4. program vypíše pozdrav i se jménem.

## Schéma průběhu

![Schéma prvního programu: pozdrav, otázka na jméno a odpověď se jménem](images/flowchart.svg){ .flowchart }

## 1. Spusť VS Code a vytvoř nový soubor

Po spuštění VS Code vytvoř nový soubor typu **Python File**. Program se píše do editoru kódu, výsledek běhu programu se potom zobrazí v terminálu.

## 2. Napiš první řádek

```python title="code/01_helloworld.py" linenums="1"
print("Hello, World!")
```

Tento řádek říká Pythonu, aby zobrazil text v uvozovkách.

## 3. Ulož program

Soubor ulož například jako `helloworld.py`. Přípona `.py` říká, že jde o program v Pythonu.

!!! tip "Přípona .py"
    Editory ji většinou doplní samy. Když ji budeš psát ručně, nezapomeň na tečku před `py`.

## 4. Spusť a zkontroluj výsledek

Program spusť tlačítkem **Run**. V terminálu by se měla objevit zpráva:

```text
Hello, World!
```

## 5. Oprav chyby

Když program neběží, zkontroluj hlavně závorky a uvozovky. Jeden znak navíc nebo jeden znak chybějící stačí k tomu, aby Python programu nerozuměl.

!!! warning "Častá chyba: `Print()` místo `print()`"
    **Proč vznikne:** Python rozlišuje malá a velká písmena.

    **Oprava:** Použij přesně `print` malými písmeny.

!!! warning "Častá chyba: Chybí uvozovka nebo závorka"
    **Proč vznikne:** Text nebo volání funkce není správně uzavřené.

    **Oprava:** Zkontroluj, že máš dvojici závorek a dvojici stejných uvozovek.

## 6. Přidej další řádky

Ve skenu se první program rozšíří tak, aby se zeptal na jméno a pak ho použil v pozdravu.

```python title="code/02_hello_person.py" linenums="1"
print("Hello, World!")
print("What's your name?")
person = input()
print("Hello,", person)
```

| Řádek | Co dělá |
| --- | --- |
| `print("Hello, World!")` | vypíše první pozdrav |
| `print("What's your name?")` | zobrazí otázku |
| `person = input()` | počká na vstup uživatele a uloží ho do proměnné `person` |
| `print("Hello,", person)` | vypíše pozdrav doplněný o zadané jméno |

!!! info "Nové slovo: proměnná"
    Proměnná je místo, kam si program uloží hodnotu. Tady se do proměnné `person` uloží jméno, které uživatel napíše.

## Zkus změnit

- Změň text prvního pozdravu.
- V druhém programu napiš místo otázky jinou větu.
- Spusť program několikrát a pokaždé zadej jiné jméno.
- Přidej ještě jeden `print()`, který vypíše vlastní větu.

## Tahák

| Zápis | K čemu slouží |
| --- | --- |
| `print("Hello, World!")` | vypíše text |
| `input()` | počká na text od uživatele |
| `person = input()` | uloží napsaný text do proměnné |
| `.py` | přípona souboru s programem v Pythonu |

## Co už umím

- [ ] umím vytvořit nový soubor ve VS Code
- [ ] umím uložit soubor s příponou `.py`
- [ ] umím spustit program tlačítkem Run
- [ ] umím opravit chybějící uvozovku nebo závorku
- [ ] umím rozšířit program o další řádky

## Shrnutí

!!! success "Zapamatuj si"
    První program ukázal, že i krátký kód má svou strukturu: příkazy, text uzavřený v uvozovkách a pořadí jednotlivých řádků.
