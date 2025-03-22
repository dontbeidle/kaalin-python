latin_uppercases = ['A', 'Á', 'B', 'D', 'E', 'F', 'G', 'Ǵ', 'H', 'X', 'Í', 'I', 'J', 'K', 'Q', 'L', 'M', 'N', 'Ń',
                    'O', 'Ó', 'P', 'R', 'S', 'T', 'U', 'Ú', 'V', 'W', 'Y', 'Z', 'Ш', 'C', 'Ch', ' ']
latin_lowercases = ['a', 'á', 'b', 'd', 'e', 'f', 'g', 'ǵ', 'h', 'x', 'ı', 'i', 'j', 'k', 'q', 'l', 'm', 'n', 'ń',
                    'o', 'ó', 'p', 'r', 's', 't', 'u', 'ú', 'v', 'w', 'y', 'z', 'sh', 'c', 'ch', ' ']

cyrillic_uppercases = ['А', 'Ә', 'Б', 'Д', 'Е', 'Ф', 'Г', 'Ғ', 'Ҳ', 'Х', 'Ы', 'И', 'Ж', 'К', 'Қ', 'Л', 'М', 'Н', 'Ң',
                   'О', 'Ө', 'П', 'Р', 'С', 'Т', 'У', 'Ү', 'В', 'Ў', 'Й', 'З', 'Ш', 'Ц', 'Ч', ' ']
cyrillic_lowercases = ['а', 'ә', 'б', 'д', 'е', 'ф', 'г', 'ғ', 'ҳ', 'х', 'ы', 'и', 'ж', 'к', 'қ', 'л', 'м', 'н', 'ң',
                   'о', 'ө', 'п', 'р', 'с', 'т', 'у', 'ү', 'в', 'ў', 'й', 'з', 'ш', 'ц', 'ч', ' ']

latin_to_cyrillic = dict(zip(latin_uppercases, cyrillic_uppercases)) | dict(zip(latin_lowercases, cyrillic_lowercases))
cyrillic_to_latin = dict(zip(cyrillic_uppercases, latin_uppercases)) | dict(zip(cyrillic_lowercases, latin_lowercases))
