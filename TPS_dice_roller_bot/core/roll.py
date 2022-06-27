from random import SystemRandom
from iteration_utilities import flatten
from .constants import DICE_ROLL_REGEX

from .parse import parse_text_regex


### roll_message(message, single_result_mode)
# takes the message and give back the rolled dices

def roll_message(message, single_result_mode=False):
    try:
        message = message.replace('/roll', '')
        message = message.replace('/r', '')
        parsed_groups = parse_text_regex(message, DICE_ROLL_REGEX)
        number, dice, mod, comment = normalize_values(list(parsed_groups))
        result, result_list = roll(number, dice, mod)
        return result, result_list, comment.strip()
    except Exception as e:
        raise e


### score_roll()
# returns a list of ability scores

def score_roll():
    score_list = []
    dice = 6
    number = 4
    mod = 0
    for i in range(0, 6):
        score_result_tmp = []
        tmp_result, tmp_result_list = roll(number, dice, mod)
        score_result_tmp.append(tmp_result_list)
        score_result = remove_minimum(score_result_tmp)
        score_list.append(score_result)
    return_list = [sum(scores) for scores in score_list]
    return return_list


### roll(dice, number, mod)
# takes three values, corresponding to: number of sides of the die, number of dice,
# modifier to the roll, returns the tuple (result, result_list)

def roll(number, dice, mod):
    if number > 100:
        raise Exception('Too many dice. Max allowed is 100')

    result_list = []
    for i in range(0, abs(number)):
        if dice >= 1:
            result_list.append(SystemRandom().randint(1, dice))
        else:
            result_list.append(SystemRandom().randint(1, 1))
    result = (sum(result_list) + mod, result_list)
    return result


### remove_minimum(input_list)
# removes the minimum element from input_list

def remove_minimum(input_list):
    input_list = list(flatten(input_list))
    input_list.remove(min(input_list))
    return input_list


### remove_minimum(input_list)
# removes the minimum element from input_list

def normalize_values(values):
    number, dice, mod, comment = values

    if number is None or number == ' ' or number == '':
        number = 1
    else:
        number = number.replace(" ", "")
    if dice is None:
        dice = 1
    else:
        dice = dice.replace(" ", "")
    if mod is None:
        mod = 0
    else:
        mod = mod.replace(" ", "")

    return int(number), int(dice), int(mod), comment
