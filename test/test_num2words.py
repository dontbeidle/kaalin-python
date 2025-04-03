import pytest
from kaalin.number.num2words import to_word
from kaalin.number.exceptions import NumberRangeError


def test_basic_numbers_latin():
    assert to_word(0) == "nol"
    assert to_word(1) == "bir"
    assert to_word(5) == "bes"
    assert to_word(10) == "on"
    assert to_word(11) == "on bir"
    assert to_word(20) == "jigirma"
    assert to_word(25) == "jigirma bes"
    assert to_word(100) == "júz"
    assert to_word(101) == "bir júz bir"


def test_basic_numbers_cyrillic():
    assert to_word(0, "cyr") == "ноль"
    assert to_word(1, "cyr") == "бир"
    assert to_word(5, "cyr") == "бес"
    assert to_word(10, "cyr") == "он"
    assert to_word(11, "cyr") == "он бир"
    assert to_word(20, "cyr") == "жигирма"
    assert to_word(25, "cyr") == "жигирма бес"
    assert to_word(100, "cyr") == "жүз"
    assert to_word(101, "cyr") == "бир жүз бир"


def test_large_numbers():
    assert to_word(1000000) == "bir million"
    assert to_word(1000000000) == "bir milliard"
    assert to_word(1000000000000) == "bir trillion"
    assert to_word(10**30) == "bir nonillion"  # Maximum supported number


def test_error_cases():
    # Test non-integer input
    with pytest.raises(TypeError):
        to_word("123")
    
    with pytest.raises(TypeError):
        to_word(123.45)
    
    # Test number exceeding limit
    with pytest.raises(NumberRangeError):
        to_word(10**30 + 1)
    
    with pytest.raises(NumberRangeError):
        to_word(-10**30 - 1)
    
    # Test invalid num_type
    with pytest.raises(KeyError):
        to_word(123, "invalid")


def test_special_cases():
    # Test numbers with multiple thousands
    assert to_word(1000000) == "bir million"
    assert to_word(1000001) == "bir million bir"
    assert to_word(1001000) == "bir million bir mıń"
    assert to_word(1001001) == "bir million bir mıń bir"
    
    # Test numbers with hundreds and thousands
    assert to_word(1100) == "bir mıń bir júz"
    assert to_word(1101) == "bir mıń bir júz bir"
    assert to_word(1111) == "bir mıń bir júz on bir" 
