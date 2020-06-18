

### parse_text(text)
# takes a string, return three values for use with roll()

def parse_text(text):
    command, equation = text.split()
    number, other = equation.split('d')
    try:
        dice, mod = other.split('+')
        result = (int(dice), int(number), int(mod))
    except Exception as e:
        print(e)
        try:
            dice, mod = other.split('-')
            result = (int(dice), int(number), -int(mod))
        except Exception as f:
            print(f)
            result = (int(other), int(number), 0)
    return result

