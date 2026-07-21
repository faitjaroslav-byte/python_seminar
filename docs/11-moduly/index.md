# 11. Moduly

<div class="lesson-meta">
<strong>Doporučený čas:</strong> 45 minut<br>
<strong>Výstup:</strong> Umíš importovat modul nebo vybranou funkci.
</div>
## Celý modul

```python
import random

number = random.randint(1, 6)
```

## Vybraná funkce

```python
from random import choice

direction = choice(["N", "S", "E", "W"])
```

## Přejmenování

```python
from time import time as current_time

print(current_time())
```

[Stáhnout ukázku](code/moduly.py){ .md-button }
