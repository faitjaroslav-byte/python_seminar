# 13. Úvod do Turtle Graphics

<div class="lesson-meta">
<strong>Doporučený čas:</strong> 60 minut<br>
<strong>Výstup:</strong> Umíš vytvořit želvu, pohybovat jí a nastavit pero.
</div>
## První kresba

```python
import turtle as t

t.forward(100)
t.right(90)
t.forward(100)
t.done()
```

## Souřadnice

Střed okna má souřadnice `(0, 0)`. Osa `x` vede vodorovně a osa `y` svisle.

## Základní příkazy

| Příkaz | Význam |
|---|---|
| `t.forward(100)` | pohyb dopředu |
| `t.right(90)` | otočení doprava |
| `t.goto(x, y)` | přesun na souřadnice |
| `t.penup()` | zvednutí pera |
| `t.pendown()` | položení pera |
| `t.color("red")` | změna barvy |

[Stáhnout ukázku](code/turtle_uvod.py){ .md-button }
