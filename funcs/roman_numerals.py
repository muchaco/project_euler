def roman_to_arabian(rom_number):
    """
    :param rom_number: string
    :return: rom_number converted to arabian numeral
    """
    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    parsed_number = []
    for i in rom_number:
        try:
            if parsed_number[-1][0] == i:
                parsed_number[-1][1] += 1
            else:
                parsed_number.append([i, 1])
        except IndexError:
            parsed_number.append([i, 1])
    # print rom_number, parsed_number
    inverses = set([])
    for i in xrange(1, len(parsed_number)):
        if roman_numbers[parsed_number[i][0]] > roman_numbers[parsed_number[i-1][0]]:
            inverses.add(i)
    # print rom_number, inverses
    num = 0
    for i in xrange(len(parsed_number)):
        if i+1 in inverses:
            continue
        if i in inverses:
            num += roman_numbers[parsed_number[i][0]] * parsed_number[i][1] - roman_numbers[parsed_number[i-1][0]] * parsed_number[i-1][1]
        else:
            num += roman_numbers[parsed_number[i][0]] * parsed_number[i][1]
    return num


def arabian_to_roman(num):
    """
    :param num: int
    :return: num converted to romanian numeral
    """
    length = len(num)
    if length == 1:
        if int(num) < 4:
            return int(num)*'I'
        elif int(num) == 4:
            return 'IV'
        elif int(num) == 5:
            return 'V'
        elif int(num) < 9:
            return 'V'+(int(num)-5)*'I'
        else:
            return 'IX'
    elif length == 2:
        if int(num[0]) < 4:
            return int(num[0]) * 'X' + arabian_to_roman(num[1])
        elif int(num[0]) == 4:
            return 'XL' + arabian_to_roman(num[1])
        elif int(num[0]) == 5:
            return 'L' + arabian_to_roman(num[1])
        elif int(num[0]) < 9:
            return 'L' + (int(num[0])-5)*'X' + arabian_to_roman(num[1])
        elif int(num[0]) == 9:
            return 'XC' + arabian_to_roman(num[1])
    elif length == 3:
        if int(num[0]) < 4:
            return int(num[0]) * 'C' + arabian_to_roman(num[1:])
        elif int(num[0]) == 4:
            return 'CD' + arabian_to_roman(num[1:])
        elif int(num[0]) == 5:
            return 'D' + arabian_to_roman(num[1:])
        elif int(num[0]) < 9:
            return 'D' + (int(num[0])-5)*'C' + arabian_to_roman(num[1:])
        elif int(num[0]) == 9:
            return 'CM' + arabian_to_roman(num[1:])
    elif length >= 4:
        return int(num[0:-3]) * 'M' + arabian_to_roman(num[-3:])