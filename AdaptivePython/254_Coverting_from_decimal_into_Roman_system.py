numerals = [
    {'letter': 'M', 'value': 1000},
    {'letter': 'D', 'value': 500},
    {'letter': 'C', 'value': 100},
    {'letter': 'L', 'value': 50},
    {'letter': 'X', 'value': 10},
    {'letter': 'V', 'value': 5},
    {'letter': 'I', 'value': 1},
]


def roman_to_arabic(number):
    index_by_letter = {}
    for index in range(len(numerals)):
        index_by_letter[numerals[index]['letter']] = index

    result = 0
    previous_value = None
    for letter in reversed(number):
        index = index_by_letter[letter]
        value = numerals[index]['value']
        if (previous_value is None) or (previous_value <= value):
            result += value
        else:
            result -= value
        previous_value = value

    return result


def arabic_to_roman(number):
    remainder = number
    result = ''
    for numeral_index in range(len(numerals)):

        #        print('-----------')
        #        print(result,'- result')
        #        print(remainder, '-rem')

        numeral = numerals[numeral_index]
        next_numeral = numerals[numeral_index + 1] if numeral_index + 1 < len(numerals) else None
        next_to_next_numeral = numerals[numeral_index + 2] if numeral_index + 2 < len(numerals) else None
        #prev_numeral = numerals[numeral_index - 1] if numeral_index - 1 > 0 else None

        #        print(numeral['value'])

        factor = remainder // numeral['value']
        remainder -= factor * numeral['value']
        if factor > 0:
            result += numeral['letter'] * factor

        if next_numeral:
            if next_to_next_numeral:
                if numeral['letter'] in ['M', 'C', 'X']:
                    if remainder >= numeral['value'] - next_to_next_numeral['value']:
                        result += next_to_next_numeral['letter'] + numeral['letter']
                        remainder -= numeral['value'] - next_to_next_numeral['value']
                        #                        print('mark1')
                        continue
                else:
                    if remainder >= numeral['value'] - next_numeral['value']:
                        result += next_numeral['letter'] + numeral['letter']
                        remainder -= numeral['value'] - next_numeral['value']
                        #                        print('mark2')
                        continue

            numeral_difference = numeral['value'] - next_numeral['value']

            #            print(remainder, '<--')

            if (remainder - numeral_difference >= 0) and (numeral_difference > next_numeral['value']):
                result += next_numeral['letter'] + numeral['letter']
                remainder -= numeral_difference

    return result

print(arabic_to_roman(int(input())))
