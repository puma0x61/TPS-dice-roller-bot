from random import choice
from .constants import PG_CREATION_PARTS
from .roll import score_roll
from .HTML_text_formatter import HTML_text_formatter as html


def pg_creation_feature():
    character_sheet = []
    for key in PG_CREATION_PARTS:
        characteristic_selected = characteristic_selector(key)
        characteristic_message = characteristic_message_creator(key, characteristic_selected)
        character_sheet.append(characteristic_message)
    character_sheet.append(ability_scores_creator())
    return '\n'.join(character_sheet)


def characteristic_selector(key):
    return choice(PG_CREATION_PARTS.get(key))


def characteristic_message_creator(key, characteristic):
    return html(key, 'bold') + ': ' + characteristic


def ability_scores_creator():
    scores = score_roll()
    ability_scores = html('Ability scores: ', 'bold') + ''.join(str(scores))
    return ability_scores 
