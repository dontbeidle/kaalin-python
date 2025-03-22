from kaalin.constants import latin_to_cyrillic, cyrillic_to_latin


def latin2cyrillic(text: str) -> str:
    """Latın jazıwın Kiril jazıwına ótkeriw"""
    text = text.replace("sh", "ш")
    text = text.replace("Sh", "Ш")
    text = text.replace("SH", "Ш")
    result = []
    i = 0
    while i < len(text):
        if i < len(text) - 1 and text[i:i+2] in latin_to_cyrillic:
            result.append(latin_to_cyrillic[text[i:i+2]])
            i += 2
        else:
            result.append(latin_to_cyrillic.get(text[i], text[i]))
            i += 1
    return ''.join(result)


def cyrillic2latin(text: str) -> str:
    """Kiril jazıwın Latın jazıwına ótkeriw"""
    text = text.replace("ш", "sh")
    text = text.replace("Ш", "Sh")
    result = []
    for char in text:
        result.append(cyrillic_to_latin.get(char, char))
    return ''.join(result)
