from math import floor
from random import choice, randrange
from .constants import PG_CREATION_PARTS, HEIGHT_TABLE, WEIGHT_TABLE
from .roll import score_roll
from .HTML_text_formatter import html_text_formatter as html


def pg_creation_feature():
    character_sheet = []
    for key in PG_CREATION_PARTS:
        characteristic_selected = characteristic_selector(key)
        characteristic_message = characteristic_message_creator(key, characteristic_selected)
        character_sheet.append(characteristic_message)
        if key == 'Race':
            character_sheet.append(heigth_message_creator(characteristic_selected))
            character_sheet.append(weigth_message_creator(characteristic_selected))
    character_sheet.append(ability_scores_creator())
    return '\n'.join(character_sheet)


def characteristic_selector(key):
    return choice(PG_CREATION_PARTS.get(key))


def characteristic_message_creator(key, characteristic):
    return html(key, 'bold') + ': ' + characteristic


def height_roll(race):
    return randrange(HEIGHT_TABLE.get(race)[0], HEIGHT_TABLE.get(race)[1])


def heigth_message_creator(race):
    try:
        height = height_roll(race)
        height_message = html('Height', 'bold') + ': ' + str(height) + 'cm, or ' + height_converter(height)
    except Exception as e:
        print(e)
        height_message = html('Height', 'bold') + ': You choose'
    return height_message


def weight_roll(race):
    weight_lbs = randrange(WEIGHT_TABLE.get(race)[0], WEIGHT_TABLE.get(race)[1])
    weight_kgs = round(weight_lbs * 0.45)
    return weight_lbs, weight_kgs


def weigth_message_creator(race):
    try:
        weight = weight_roll(race)
        weight_message = html('Weight', 'bold') + ': ' + str(weight[1]) + 'kg, or ' + str(weight[0]) + 'lbs'
    except:
        weight_message = html('Weight', 'bold') + ': You choose'
    return weight_message


def ability_scores_creator():
    scores = score_roll()
    ability_scores = html('Ability scores: ', 'bold') + ''.join(str(scores))
    return ability_scores


def height_converter(height_cm):
    height_inch = height_cm / 2.54
    height_ft = floor(height_inch / 12)
    remaining_inches = round(height_inch % 12)
    return str(height_ft) + 'feet, ' + str(remaining_inches) + 'inches'


