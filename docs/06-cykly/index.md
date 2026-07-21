# 6. Cykly

<div class="lesson-meta">
<strong>Doporučený čas:</strong> 75 minut<br>
<strong>Výstup:</strong> Umíš opakovat příkazy pomocí `for` a `while`.
</div>
## Cyklus `for`

```python
for number in range(5):
    print(number)
```

## Cyklus `while`

```python
lives = 3

while lives > 0:
    print("Zbývá životů:", lives)
    lives -= 1
```

!!! danger "Nekonečný cyklus"
    Podmínka cyklu `while` se musí během programu někdy změnit.

[Stáhnout ukázku](code/cykly.py){ .md-button }
