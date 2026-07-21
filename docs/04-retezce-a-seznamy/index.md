# 4. Řetězce a seznamy

<div class="lesson-meta">
<strong>Doporučený čas:</strong> 60 minut<br>
<strong>Výstup:</strong> Umíš pracovat s textem, indexem a seznamem.
</div>
## Řetězec

```python
word = "python"
print(len(word))
print(word[0])
```

## Seznam

```python
animals = ["kočka", "pes", "vydra"]
print(animals[1])
animals.append("sova")
```

## Náhodný prvek

```python
from random import choice

print(choice(animals))
```

[Stáhnout ukázku](code/seznamy.py){ .md-button }
