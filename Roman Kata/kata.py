# Kata for Roman Numerals

class RomanNum:

    # Mappings
    roman_to_arabic = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    arabic_to_roman = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    @classmethod
    def to_roman(cls, num):
        """Convert Arabic number to Roman numeral."""
        roman_numeral = ''
        while num > 0:
            for i, r in cls.arabic_to_roman:
                while num >= i:
                    roman_numeral += r
                    num -= i
        return roman_numeral

    @classmethod
    def from_roman(cls, roman_numeral):
        """Convert Roman numeral to Arabic number."""
        i = 0
        num = 0
        while i < len(roman_numeral):
            if (i+1 < len(roman_numeral) and
                    cls.roman_to_arabic[roman_numeral[i]] < cls.roman_to_arabic[roman_numeral[i+1]]):
                num += cls.roman_to_arabic[roman_numeral[i+1]
                                           ] - cls.roman_to_arabic[roman_numeral[i]]
                i += 2
            else:
                num += cls.roman_to_arabic[roman_numeral[i]]
                i += 1
        return num


print(RomanNum.to_roman(1123))  # used to test outcomes
print(RomanNum.from_roman("MXIII"))  # used to test outcomes
