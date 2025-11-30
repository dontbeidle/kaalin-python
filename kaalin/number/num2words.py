from .exceptions import NumberRangeError


def to_word(number: int | float, num_type: str = "lat") -> str:
    """
    Convert an integer or float to its text representation in either Latin or Cyrillic script.

    Args:
        number: The integer or float to convert
        num_type: The type of script to use, either "lat" or "cyr"

    Returns:
        The textual representation of the number

    Raises:
        NumberRangeError: If the number exceeds the maximum supported number (nonillion)
    """

    _NUM_TYPE_LAT = 'lat'
    _NUM_TYPE_CYR = 'cyr'
    _KEY_ONES = 'ones'
    _KEY_TEENS = 'teens'
    _KEY_TENS = 'tens'
    _KEY_HUNDRED = 'hundred'
    _KEY_THOUSANDS = 'thousands'
    _KEY_MINUS_SIGN = 'minus'
    _KEY_PUTIN = 'putin'
    _KEY_DENOMINATORS = 'denominators'

    _locale = {
        _NUM_TYPE_LAT: {
            _KEY_ONES: ['nol', 'bir', 'eki', 'úsh', 'tórt', 'bes', 'altı', 'jeti', 'segiz', 'toǵız'],
            _KEY_TEENS: ['on bir', 'on eki', 'on úsh', 'on tórt', 'on bes', 'on altı', 'on jeti', 'on segiz', 'on toǵız'],
            _KEY_TENS: ['on', 'jigirma', 'otız', 'qırıq', 'eliw', 'alpıs', 'jetpis', 'seksen', 'toqsan'],
            _KEY_THOUSANDS: ['', 'mıń', 'million', 'milliard', 'trillion', 'kvadrillion', 'kvintillion', 'sekstilion', 'septillion', 'oktillion', 'nonillion'],
            _KEY_HUNDRED: 'júz',
            _KEY_MINUS_SIGN: 'minus',
            _KEY_PUTIN: 'pútin',
            _KEY_DENOMINATORS: {
                10: 'onnan',
                100: 'júzden',
                1000: 'mıńnan',
                10000: 'on mıńnan',
                100000: 'júz mıńnan',
                1000000: 'millionnan',
                10000000: 'on millionnan',
                100000000: 'júz millionnan',
                1000000000: 'milliardtan',
                10000000000: 'on milliardtan',
                100000000000: 'júz milliardtan',
                1000000000000: 'trillionnan',
                10000000000000: 'on trillionnan',
                100000000000000: 'júz trillionnan',
                1000000000000000: 'kvadrillionnan',
                10000000000000000: 'on kvadrillionnan',
                100000000000000000: 'júz kvadrillionnan',
                1000000000000000000: 'kvintillionnan',
                10000000000000000000: 'on kvintillionnan',
                100000000000000000000: 'júz kvintillionnan',
                1000000000000000000000: 'sekstilionnan',
                10000000000000000000000: 'on sekstilionnan',
                100000000000000000000000: 'júz sekstilionnan',
                1000000000000000000000000: 'septillionnan',
                10000000000000000000000000: 'on septillionnan',
                100000000000000000000000000: 'júz septillionnan',
                1000000000000000000000000000: 'oktillionnan',
                10000000000000000000000000000: 'on oktillionnan',
                100000000000000000000000000000: 'júz oktillionnan',
                1000000000000000000000000000000: 'nonillionnan',
            }
        },
        _NUM_TYPE_CYR: {
            _KEY_ONES: ['ноль', 'бир', 'еки', 'үш', 'төрт', 'бес', 'алты', 'жети', 'сегиз', 'тоғыз'],
            _KEY_TEENS: ['он бир', 'он еки', 'он үш', 'он төрт', 'он бес', 'он алты', 'он жети', 'он сегиз', 'он тоғыз'],
            _KEY_TENS: ['он', 'жигирма', 'отыз', 'қырық', 'елиў', 'алпыс', 'жетпис', 'сексен', 'тоқсан'],
            _KEY_THOUSANDS: ['', 'мың', 'миллион', 'миллиард', 'триллион', 'квадриллион', 'квинтиллион', 'секстиллион', 'септиллион', 'октиллион', 'нониллион'],
            _KEY_HUNDRED: 'жүз',
            _KEY_MINUS_SIGN: 'минус',
            _KEY_PUTIN: 'пүтин',
            _KEY_DENOMINATORS: {
                10: 'оннан',
                100: 'жүзден',
                1000: 'мыңнан',
                10000: 'он мыңнан',
                100000: 'жүз мыңнан',
                1000000: 'миллионнан',
                10000000: 'он миллионнан',
                100000000: 'жүз миллионнан',
                1000000000: 'миллиардтан',
                10000000000: 'он миллиардтан',
                100000000000: 'жүз миллиардтан',
                1000000000000: 'триллионнан',
                10000000000000: 'он триллионнан',
                100000000000000: 'жүз триллионнан',
                1000000000000000: 'квадриллионнан',
                10000000000000000: 'он квадриллионнан',
                100000000000000000: 'жүз квадриллионнан',
                1000000000000000000: 'квинтиллионнан',
                10000000000000000000: 'он квинтиллионнан',
                100000000000000000000: 'жүз квинтиллионнан',
                1000000000000000000000: 'секстиллионнан',
                10000000000000000000000: 'он секстиллионнан',
                100000000000000000000000: 'жүз секстиллионнан',
                1000000000000000000000000: 'септиллионнан',
                10000000000000000000000000: 'он септиллионнан',
                100000000000000000000000000: 'жүз септиллионнан',
                1000000000000000000000000000: 'октиллионнан',
                10000000000000000000000000000: 'он октиллионнан',
                100000000000000000000000000000: 'жүз октиллионнан',
                1000000000000000000000000000000: 'нониллионнан',
            }
        }
    }

    if num_type not in ['lat', 'cyr']:
        raise KeyError("Invalid num_type")

    if not isinstance(number, (int, float)):
        raise TypeError("Input must be an integer or float")

    is_negative = number < 0
    number = abs(number)

    # Check if number exceeds nonillion (10^30)
    if number > 10**30:
        raise NumberRangeError("Number exceeded limit")

    current_locale = _locale[_NUM_TYPE_CYR] if num_type == _NUM_TYPE_CYR else _locale[_NUM_TYPE_LAT]

    ones = current_locale[_KEY_ONES]
    teens = current_locale[_KEY_TEENS]
    tens = current_locale[_KEY_TENS]
    thousands = current_locale[_KEY_THOUSANDS]
    minus_sign = current_locale[_KEY_MINUS_SIGN]
    putin = current_locale[_KEY_PUTIN]
    denominators = current_locale[_KEY_DENOMINATORS]

    def convert_hundreds(num):
        if num < 10:
            return ones[num]
        elif 10 < num < 20:
            return teens[num - 11]
        elif num < 100:
            return tens[num // 10 - 1] + (" " + ones[num % 10] if num % 10 != 0 else "")
        else:
            return ones[num // 100] + f" {current_locale[_KEY_HUNDRED]}" + (" " + convert_hundreds(num % 100) if num % 100 != 0 else "")

    def convert_integer(num):
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

    def convert_float(num):
        # Split into integer and fractional parts
        str_num = str(num)
        if '.' in str_num:
            int_part, frac_part = str_num.split('.')
        else:
            # Handle scientific notation
            int_part = str(int(num))
            frac_part = str(num).split('.')[-1] if '.' in str(num) else '0'
        
        int_value = int(int_part)
        frac_value = int(frac_part)
        
        # Calculate denominator (10, 100, 1000, etc.)
        denominator = 10 ** len(frac_part)
        
        # Convert parts
        int_word = convert_integer(int_value)
        frac_word = convert_integer(frac_value)
        
        # Get denominator word
        denominator_word = denominators.get(denominator, f"{convert_integer(denominator)}nan")
        
        result = f"{int_word} {putin} {denominator_word} {frac_word}"
        
        if is_negative:
            result = f"{minus_sign} {result}"
        
        return result

    # Handle float vs integer
    if isinstance(number, float):
        return convert_float(number)
    else:
        result = convert_integer(number)
        if is_negative:
            result = f"{minus_sign} {result}"
        return result