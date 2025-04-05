from .exceptions import NumberRangeError


def to_word(number: int, num_type: str = "lat") -> str:
    """
    Convert an integer to its text representation in either Latin or Cyrillic script.
    
    Args:
        number: The integer to convert
        num_type: The type of script to use, either "lat" or "cyr"
        
    Returns:
        The textual representation of the integer
        
    Raises:
        NumberRangeError: If the input is not an integer or exceeds the maximum supported number (nonillion)
    """

    _NUM_TYPE_LAT = 'lat'
    _NUM_TYPE_CYR = 'cyr'
    _KEY_ONES = 'ones'
    _KEY_TEENS = 'teens'
    _KEY_TENS = 'tens'
    _KEY_HUNDRED = 'hundred'
    _KEY_THOUSANDS = 'thousands'

    _locale = {
        _NUM_TYPE_LAT: {
            _KEY_ONES: ['nol', 'bir', 'eki', 'úsh', 'tórt', 'bes', 'altı', 'jeti', 'segiz', 'toǵız'],
            _KEY_TEENS: ['on bir', 'on eki', 'on úsh', 'on tórt', 'on bes', 'on altı', 'on jeti', 'on segiz', 'on toǵız'],
            _KEY_TENS: ['on', 'jigirma', 'otız', 'qırıq', 'eliw', 'alpıs', 'jetpis', 'seksen', 'toqsan'],
            _KEY_THOUSANDS: ['', 'mıń', 'million', 'milliard', 'trillion', 'kvadrillion', 'kvintillion', 'sekstilion', 'septillion', 'oktillion', 'nonillion'],
            _KEY_HUNDRED: 'júz',
        },
        _NUM_TYPE_CYR: {
            _KEY_ONES: ['ноль', 'бир', 'еки', 'үш', 'төрт', 'бес', 'алты', 'жети', 'сегиз', 'тоғыз'],
            _KEY_TEENS: ['он бир', 'он еки', 'он үш', 'он төрт', 'он бес', 'он алты', 'он жети', 'он сегиз', 'он тоғыз'],
            _KEY_TENS: ['он', 'жигирма', 'отыз', 'қырық', 'елиў', 'алпыс', 'жетпис', 'сексен', 'тоқсан'],
            _KEY_THOUSANDS: ['', 'мың', 'миллион', 'миллиард', 'триллион', 'квадриллион', 'квинтиллион', 'секстиллион', 'септиллион', 'октиллион', 'нониллион'],
            _KEY_HUNDRED: 'жүз',
        }
    }
    
    if num_type not in ['lat', 'cyr']:
        raise KeyError("Invalid num_type")
    
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
        
    # Check if number exceeds nonillion (10^30)
    if abs(number) > 10**30:
        raise NumberRangeError("Number exceeded limit")
    
    current_locale = _locale[_NUM_TYPE_CYR] if num_type == _NUM_TYPE_CYR else _locale[_NUM_TYPE_LAT]
    
    ones = current_locale[_KEY_ONES]
    teens = current_locale[_KEY_TEENS]
    tens = current_locale[_KEY_TENS]
    thousands = current_locale[_KEY_THOUSANDS]

    def convert_hundreds(num):
        if num < 10:
            return ones[num]
        elif 10 < num < 20:
            return teens[num - 11]
        elif num < 100:
            return tens[num // 10 - 1] + (" " + ones[num % 10] if num % 10 != 0 else "")
        else:
            return ones[num // 100] + f" {current_locale[_KEY_HUNDRED]}" + (" " + convert_hundreds(num % 100) if num % 100 != 0 else "")

    def convert_number(num):
        if num == 0:
            return ones[num]
        if num == 100:
            return current_locale[_KEY_HUNDRED]
        if num == 1000:
            return thousands[1]

        parts = []
        i = 0
        while num > 0:
            if num % 1000 != 0:
                parts.append(convert_hundreds(num % 1000) + (" " + thousands[i] if thousands[i] else ""))
            num //= 1000
            i += 1
        return " ".join(reversed(parts))

    return convert_number(number)
