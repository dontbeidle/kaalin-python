# Kaalin

<p>
    Using this library, certain operations for the Karakalpak language can be performed very quickly and conveniently.
</p>

## Example
```python
from kaalin.converter import latin2cyrillic, cyrillic2latin


print(latin2cyrillic("Assalawma áleykum"))      # Ассалаўма әлейкум
print(cyrillic2latin("Ассалаўма әлейкум"))      # Assalawma áleykum
```

```python
from kaalin.number import to_word, NumberRangeError


try:
  print(to_word(123))                     # bir júz jigirma úsh
  print(to_word(999, num_type="cyr"))     # тоғыз жүз тоқсан тоғыз
except NumberRangeError as e:
  print("San shegaradan asıp ketti!")
```

```python
from kaalin.string import upper, lower


print(upper("Assalawma áleykum"))     # ASSALAWMA ÁLEYKUM
print(lower("Assalawma áleykum"))     # assalawma áleykum
```
