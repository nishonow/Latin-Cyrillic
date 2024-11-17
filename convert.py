# uzbek latin to uzbek cyrillic function

lat_to_cyr = {
    "A": "А", "B": "Б", "V": "В", "G": "Г", "D": "Д", "Ye": "Е", "YE": "Е",
    "J": "Ж", "Z": "З", "I": "И", "Y": "Й", "K": "К", "L": "Л", "M": "М",
    "N": "Н", "O": "О", "P": "П", "R": "Р", "S": "С", "T": "Т", "U": "У",
    "F": "Ф", "X": "Х", "Ts": "Ц", "TS": "Ц", "Ch": "Ч", "CH": "Ч",
    "Sh": "Ш", "EE": "Э", "Yu": "Ю", "YU": "Ю", "Ya": "Я",
    "G'": "Ғ", "O'": "Ў", "O’": "Ў", "Yo": "Ё",
    "Q": "Қ", "H": "Ҳ", "a": "а", "b": "б", "v": "в", "g": "г", "d": "д",
    "ye": "е", "j": "ж", "z": "з", "i": "и", "y": "й", "k": "к",
    "l": "л", "m": "м", "n": "н", "o": "о", "p": "п", "r": "р", "s": "с",
    "t": "т", "u": "у", "f": "ф", "x": "х", "ts": "ц", "ch": "ч",
    "sh": "ш", "'": "ъ", "ee": "э",
    "e": "е", "yu": "ю", "ya": "я", "o'": "ў",
    "q": "қ", "g'": "ғ", "yo": "ё", "h": "ҳ"
}

cyr_to_lat = {v: k for k, v in lat_to_cyr.items()}



def latin_to_cyrillic(text):
    result = ""
    i = 0
    while i < len(text):
        two_char = text[i:i + 2]
        if two_char in lat_to_cyr:
            result += lat_to_cyr[two_char]
            i += 2
        else:
            result += lat_to_cyr.get(text[i], text[i])
            i += 1
    return result

def cyrillic_to_latin(text):
    result = ""
    i = 0
    while i < len(text):
        char = text[i]
        if i + 1 < len(text):
            two_char = text[i:i + 2]
            if two_char in cyr_to_lat:
                result += cyr_to_lat[two_char]
                i += 2
                continue
        result += cyr_to_lat.get(char, char)
        i += 1
    return result
