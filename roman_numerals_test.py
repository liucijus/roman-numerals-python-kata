def to_roman(number):
    rules = [
            (1000, 'M'), 
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'), 
            (4, 'IV'),
            (1, 'I')
            ]

    def convert_to_roman(number, rules):
        if rules:
            arabic, roman = rules[0]
            times = number / arabic

            return roman * times + convert_to_roman(number % arabic, rules[1:]) 
        else:
            return ''

    return convert_to_roman(number, rules)

tests = [
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, 'V'),
        (6, 'VI'),
        (9, 'IX'),
        (10, 'X'),
        (16, 'XVI'),
        (20, 'XX'),
        (40, 'XL'),
        (50, 'L'),
        (90, 'XC'),
        (100, 'C'),
        (400, 'CD'),
        (500, 'D'),
        (900, 'CM'),
        (1000, 'M')
        ]

def test_arabic_to_roman_conversion():
    for (arabic, roman) in tests:
        assert to_roman(arabic) == roman

