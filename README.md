# Kaalin

<p>
    The string methods provided by the Python programming language are primarily tailored for English language usage, which might not seamlessly suit the needs of other languages such as Karakalpak. Consequently, to bridge this gap, you can employ this library to avail a range of functions specifically designed to accommodate the intricacies of the Karakalpak language. 
</p>

## Example
```python
from kaalin import Latin

kaa = Latin('BÁHÁR')

print(kaa.upper())      # BÁHÁR
print(kaa.lower())      # báhár
print(kaa.isupper())    # True
print(kaa.islower())    # False
print(kaa.isalpha())    # True
print(kaa.isdigit())    # False
```

```python
from kaalin import NumberLatin, NumberRangeError, NumberCyrillic

kaa_num_latin = NumberLatin()
kaa_num_cyrillic = NumberCyrillic()

try:
  print(kaa_num_latin.to_words(533_525))  # bes júz otız úsh mıń bes júz jigirma bes
  print(kaa_num_latin.to_words(894_236_671))  # segiz júz toqsan tórt million eki júz otız altı mıń altı júz jetpis bir
  print(kaa_num_cyrillic.to_words(9_324)) # тоғыз мың үш жүз жигирма төрт
  print(kaa_num_cyrillic.to_words(1_324_572_942)) # бир миллиард үш жүз жигирма төрт миллион бес жүз жетпис еки мың тоғыз жүз қырық еки
except NumberRangeError as e:
  print("San shegaradan asıp ketti!")
```
```python
from kaalin.converter import latin2cyrillic, cyrillic2latin


print(latin2cyrillic("Assalawma áleykum"))      # Ассалаўма әлейкум
print(cyrillic2latin("Ассалаўма әлейкум"))      # Assalawma áleykum
```
```python
from kaalin.string import upper, lower

print(upper("Assalawma áleykum")) 	  # ASSALAWMA ÁLEYKUM
print(lower("Assalawma áleykum"))     # assalawma áleykum
```
```python
from kaalin.number import to_word

print(to_word(2025))                      # eki mıń jigirma bes
print(to_word(2025, num_type='cyr'))      # еки мың жигирма бес
```
