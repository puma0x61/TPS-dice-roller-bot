from random import choices, choice

from .constants import FABULA_THEME, FABULA_CONCEPT, FABULA_DETAIL, FABULA_ADJECTIVES


def fabula_pg_feature():
    return fabula_message_creator({
        'theme': choice(FABULA_THEME),
        'concept': choice(FABULA_CONCEPT),
        'adjectives': choices(FABULA_ADJECTIVES, k=2),
        'detail': choice(FABULA_DETAIL)
    })


def fabula_message_creator(pg):
    try:
        if pg['adjectives'][0][0] in 'aeiou':
            article = 'an'
        else:
            article = 'a'
        message = f'You are {article} {pg["adjectives"][0]} and {pg["adjectives"][1]} ' \
                  f'{pg["concept"]} {pg["detail"]}, and yours is a tale of {pg["theme"]}.'
    except Exception as e:
        print(e)
        message = 'There\'s been a mistake. It\'s you.'
    return message
