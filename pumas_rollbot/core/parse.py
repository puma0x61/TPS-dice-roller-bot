### parse_text(text)
# takes a string, return three values for use with roll()

def parse_text(text):
    # "/r"," d20 + 4"
    # "/r"," 1d20 + 4"
    command, equation = text.split()
    # " ","20 + 4"
    # " 1","20 + 4"
    number, other = equation.split('d')
    try:
        # "20 "," 4"
        if '+' in other:
            dice, mod = other.split('+')
        elif '-' in other:
            dice, mod = other.split('-')
        else:
            dice, mod = {other, '0'}

        # "","20","4"
        # "1","20","4"
        # In this way we can have spaces in the message
        number = number.strip()
        dice = dice.strip()
        mod = mod.strip()

        if number != '':
            result = (int(dice), int(number), int(mod))
        else:
            result = (int(dice), 1, int(mod))
    except Exception as e:
        print(e)
        return (0, 0, 0)

    return result
