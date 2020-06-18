### parse_text(text)
# takes a string, return three values for use with roll()

def parse_text(text):
    command, equation = text.split()
    number, other = equation.split('d')
    try:
        if '+' in other:
            dice, mod = other.split('+')
        else:
            dice, mod = {other, 0}
        if(number != ''):
            result = (int(dice), int(number), int(mod))
        else:
            result = (int(dice), 1, int(mod))
    except Exception as e:
        print(e)
        try:
            dice, mod = other.split('-')
            result = (int(dice), int(number), -int(mod))
        except Exception as f:
            print(f)
            result = (int(other), int(number), 0)
    return result

