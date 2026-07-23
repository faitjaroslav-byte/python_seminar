# Lekce 6 - Projekt Zvířecí kvíz

<div class="lesson-meta">
<strong>Doporučený čas:</strong> 90-120 minut<br>
<strong>Výstup lekce:</strong> Student sestaví projekt Animal Quiz se skóre, kontrolní funkcí, více otázkami, ignorováním velikosti písmen a třemi pokusy.<br>
<strong>Zdrojová předloha:</strong> Python-first steps-p.51, strany 36-43, projekt Animal Quiz
</div>

## Co se dnes naučíš

- založit projekt `animal_quiz.py`
- ukládat skóre do proměnné `score`
- položit otázku pomocí `input()`
- vytvořit funkci `check_guess()`
- použít `global score`
- vypsat konečné skóre
- ignorovat rozdíl mezi velkými a malými písmeny
- dát hráči až tři pokusy

## Proč to potřebujeme

Projekt Animal Quiz spojuje všechno, co už se objevilo v předchozích lekcích: proměnné, vstup, podmínky, cykly a funkce. Výsledkem je krátký kvíz, který se dá snadno upravit na jiné téma.

!!! info "Důležitá myšlenka"
    Každá otázka má stejný postup: položit otázku, načíst odpověď, zkontrolovat ji a případně přičíst bod.

!!! example "Projekt podle PDF"
    Ve zdroji je kvíz o zvířatech. Otázky jsou například na ledního medvěda, geparda a plejtváka obrovského.

## Analýza projektu

- vstupem jsou odpovědi hráče
- program uchovává skóre v proměnné `score`
- funkce `check_guess()` porovnává odpověď se správnou hodnotou
- po špatné odpovědi může hráč zkusit odpovědět znovu
- na konci program zobrazí výsledné skóre

## Schéma průběhu

![Projekt Animal Quiz - průběh otázky, kontroly odpovědi, přičtení skóre a rozhodnutí o další otázce](images/flowchart.svg){ .flowchart }

## 1. Založ nový soubor

V IDLE vytvoř nový soubor a ulož ho jako `animal_quiz.py`.

## 2. Připrav skóre a úvod

```python
score = 0

print("Guess the Animal!")
```

Proměnná `score` bude sledovat počet správných odpovědí.

## 3. Přidej první otázky

```python title="code/01_animal_quiz.py" linenums="1"
score = 0

print("Guess the Animal!")

guess1 = input("Which bear lives at the North Pole? ")
if guess1 == "polar bear":
    print("Correct answer")
    score = score + 1

guess2 = input("Which is the fastest land animal? ")
if guess2 == "cheetah":
    print("Correct answer")
    score = score + 1

guess3 = input("Which is the largest animal? ")
if guess3 == "blue whale":
    print("Correct answer")
    score = score + 1

print("Your score is " + str(score))
```

## 4. Vytvoř funkci pro kontrolu

Opakovanou kontrolu přesuneme do funkce `check_guess()`.

```python title="code/02_check_guess.py" linenums="1"
score = 0

def check_guess(guess, answer):
    global score
    if guess == answer:
        print("Correct answer")
        score = score + 1

print("Guess the Animal!")

guess1 = input("Which bear lives at the North Pole? ")
check_guess(guess1, "polar bear")

guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, "cheetah")

guess3 = input("Which is the largest animal? ")
check_guess(guess3, "blue whale")

print("Your score is " + str(score))
```

| Část programu | Význam |
| --- | --- |
| `def check_guess(guess, answer):` | funkce dostane tip hráče a správnou odpověď |
| `global score` | dovolí funkci měnit proměnnou `score` |
| `check_guess(guess1, "polar bear")` | zavolá funkci pro první otázku |
| `str(score)` | převede skóre na text pro závěrečný výpis |

## 5. Ignoruj velikost písmen a přidej pokusy

Na straně 41 se projekt rozšíří tak, aby hráč dostal tři pokusy a aby nezáleželo na velkých a malých písmenech.

```python title="code/03_attempts.py" linenums="1"
score = 0

def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0

    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry, wrong answer. Try again. ")
            attempt = attempt + 1

    if attempt == 3:
        print("The correct answer is " + answer)

print("Guess the Animal!")

guess1 = input("Which bear lives at the North Pole? ")
check_guess(guess1, "polar bear")

guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, "cheetah")

guess3 = input("Which is the largest animal? ")
check_guess(guess3, "blue whale")

print("Your score is " + str(score))
```

## Hacky a úpravy

Ve zdroji je projekt záměrně otevřený k úpravám:

- přidej další otázky,
- změň téma kvízu,
- udělej kvíz s více možnými odpověďmi,
- zlepši bodování za druhý nebo třetí pokus,
- ověř, že se původní hra nepokazila.

## Časté chyby

!!! warning "Častá chyba: Zapomeneš `global score`"
    **Proč vznikne:** Funkce pak nemůže správně změnit proměnnou `score`, která je mimo funkci.

    **Oprava:** Na začátek funkce `check_guess()` přidej `global score`.

!!! warning "Častá chyba: Odpověď se porovnává moc přísně"
    **Proč vznikne:** `Polar Bear` a `polar bear` nejsou stejný řetězec.

    **Oprava:** Při porovnání použij `.lower()`.

## Tahák

| Zápis | K čemu slouží |
| --- | --- |
| `score = 0` | počáteční skóre |
| `input(...)` | otázka pro hráče |
| `def check_guess(guess, answer):` | funkce pro kontrolu odpovědi |
| `global score` | změna skóre uvnitř funkce |
| `guess.lower()` | převod odpovědi na malá písmena |
| `while still_guessing and attempt < 3:` | nejvýše tři pokusy |

## Co už umím

- [ ] umím založit projektový soubor
- [ ] umím sledovat skóre
- [ ] umím napsat funkci pro kontrolu odpovědi
- [ ] umím zavolat funkci s různými otázkami
- [ ] umím použít `.lower()`
- [ ] umím přidat omezený počet pokusů

## Shrnutí

!!! success "Zapamatuj si"
    Animal Quiz roste po malých krocích. Nejprve má otázky a skóre, potom funkci pro kontrolu, potom výpis skóre, ignorování velikosti písmen a nakonec více pokusů.
