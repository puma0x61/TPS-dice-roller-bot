#! /usr/bin/python

import telebot
from random import randint
from iteration_utilities import flatten

### TODO:
# penis size
# help message
# tit request

TOKEN = '1190003676:AAFYarLWv57VUBLituGun4uLe_MD0Xs4TWg'
HELP_MESSAGE = ('I can roll dice and do funny stuff!\n\n'
                'You can control me by sending these commands:\n\n'
                '/help -- sends this help message\n'
                '/start -- sends this help message\n\n'
                'To roll dice (each command has a long and short version):\n\n'
                '/roll -- roll dice as indicated using dice notation\n'
                '/r -- short version\n\n'
                '/ability_scores -- rolls six ability scores for use in D&D style game systems\n'
                '/as -- short version\n')


bot = telebot.TeleBot(TOKEN)


### roll(dice, number, mod)
# takes three values, corresponding to: number of sides of the die, number of dice,
# modifier to the roll, returns the tuple (result, result_list)

def roll(dice, number, mod):
    result_list = []
    for i in range(0, number):
        result_list.append(randint(1, dice))
    result = sum(result_list) + mod
    return (result, result_list)


### score_roll()

def score_roll():
    score_list = []
    dice = 6
    number = 4
    mod = 0
    for i in range(0, 6):
        score_result_tmp = []
        tmp_result, tmp_result_list = roll(dice, number, mod)
        score_result_tmp.append(tmp_result_list)
        score_result = remove_minimum(score_result_tmp)
        score_list.append(score_result)
    return_list = list(flatten([[sum(scores) for scores in sub_list] for sub_list in score_list]))
    return return_list


def remove_minimum(input_list):
    output_list = []
    for sub_list in input_list:
        minimum_index = 0
        new_sub_list = []
        for i, n in enumerate(sub_list):
            if n < sub_list[minimum_index]: minimum_index = i
        for i, n in enumerate(sub_list):
            if i == minimum_index:
                continue
            else:
                new_sub_list.append(n)
        output_list.append(new_sub_list)
    return output_list


### parse_text(text)
# takes a string, return three values for use with roll()

def parse_text(text):
    command, equation = text.split()
    number, other = equation.split('d')
    try:
        dice, mod = other.split('+')
        return (int(dice), int(number), int(mod))
    except Exception as e:
        print(e)
    return (int(other), int(number), 0)


@bot.message_handler(commands=['help', 'start'])
def welcome(message):
    bot.reply_to(message, HELP_MESSAGE)
    pass


### handle_roll(message)
# handler for the commands /roll, /r

@bot.message_handler(commands=['roll', 'r'])
def handle_roll(message):
    try:
        name = message.from_user.username
        dice, number, mod = parse_text(message.text)
        result, result_list = roll(dice, number, mod)    
        response = f'@{name} rolled {result}, ({result_list})'
    except Exception as e:
        print(e)
        print(message)
        response = 'Eh?'
    bot.reply_to(message, response)
    pass


### handle_score

@bot.message_handler(commands=['ability_scores', 'as'])
def handle_score(message):
    name = message.from_user.username
    score_list = score_roll()
    ability_scores = f'@{name} rolled {score_list}'
    bot.reply_to(message, ability_scores)
    pass


### debug: used to get file_id of a single sticker
# @bot.message_handler(content_types=["sticker"])
# def handle_sticker(message):
#     print(message)


### handle_pelor(message)
# answers to messages containing "pelor" with the right sticker

@bot.message_handler(regexp="pelor")
def handle_pelor(message):
    chat_id = message.chat.id
    bot.send_sticker(chat_id, "CAACAgQAAxkBAANDXuZB7Nb-rImmxXLfiWVXqj2OG5UAAjwAAy_0Wg-jNOhAndo8mxoE")
    pass

bot.polling()
