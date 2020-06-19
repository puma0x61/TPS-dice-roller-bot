### parse_text(text)
# takes a string, return three values for use with roll()

def parse_text(text):
    command, equation = text.split(' ')
    number, other = equation.split('d')
    try:
        if '+' in other:
            dice, mod = other.split('+')
        elif '-' in other:
            dice, mod = other.split('-')
            mod = '-' + mod
        else:
            dice, mod = other, '0'

        if len(number) == 0:
            number = '1'
        if int(number) < 0:
            result = (int(0), int(0), int(0))
        else:
            result = (int(dice), int(number), int(mod))
    except Exception as e:
        print(e)
        return (int(0), int(0), int(0))

    return result
