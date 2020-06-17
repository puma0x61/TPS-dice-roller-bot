#! /usr/bin/python

import telebot
import math
import json
from random import randint
from iteration_utilities import flatten

### TODO:
# tit request

HELP_MESSAGE = ('I can roll dice and do funny stuff!\n\n'
                'You can control me by sending these commands:\n\n'
                '/help - sends this help message\n'
                '/start - sends this help message\n\n'
                'To roll dice (each command has a long and short version):\n\n'
                '/roll - roll dice as indicated using dice notation\n'
                '/r - short version\n\n'
                '/ability_scores - rolls six ability scores for use in D&D style game systems\n'
                '/as - short version\n\n'
                '/penis_size - rolls your penis size, using the formula 10+log2(n)+CHA\n'
                '/ps - short version\n\n'
                '/spongebob - takes your message and gives you the salty version of it\n'
                '/sp - short version\n')

config = json.load(open('config.json'))
if config['bot']:
    bot = telebot.TeleBot(token=config['bot'])
else:
    print ("###################################################")
    print ("# Please setup the needed keys in the config file #")
    print ("###################################################")
    sys.exit()

### roll(dice, number, mod)
# takes three values, corresponding to: number of sides of the die, number of dice,
# modifier to the roll, returns the tuple (result, result_list)

def roll(dice, number, mod, single_result_mode=False):
    if number > 100:
       raise Exception('Too many dice. Max allowed is 100')
    else:
        result_list = []
        for i in range(0, abs(number)):
            result_list.append(randint(1, abs(dice)))
        if single_result_mode:
            result = sum(result_list) + mod
        else:
            result = (sum(result_list) + mod, result_list)
    return result


### score_roll()
# returns a list of ability scores

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
    return_list = [sum(scores) for scores in score_list]
    return return_list


### remove_minimum(input_list)
# removes the minimum element from input_list

def remove_minimum(input_list):
    input_list = list(flatten(input_list))
    input_list.remove(min(input_list))
    return input_list


### roll_penis(mod)
# rolls a d20 to decide the penis_size of a pc

def roll_penis(mod):
    die = roll(20, 1, 0, True)
    if die == 20:
        result = (die, 'mandingo')
    elif die == 1:
        result = (die, 'micropenis')
    else:
        result = (die, 10 + math.log2(die) + mod)
        if result[1] < 6:
            result = (die, 'weird')
    return result


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


### spongebob_parser(text)
# takes a string, return the same string with alternating uppercase and lowercase characters

def spongebob_parser(text):
    spongebob_sentence = ""
    for idx, char in list(enumerate(text.lower())):
        if idx % 2 == 0:
            spongebob_sentence.append(char.upper())
        else:
            spongebob_sentence.append(char)
    return spongebob_sentence

### welcome(message)
# sends HELP_MESSAGE

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
        response = 'eh?'
    bot.reply_to(message, response)
    pass


### handle_score
# handler for the commands /ability_scores, /as

@bot.message_handler(commands=['ability_scores', 'as'])
def handle_score(message):
    name = message.from_user.username
    score_list = score_roll()
    ability_scores = f'@{name} rolled {score_list}'
    bot.reply_to(message, ability_scores)
    pass


### handle_score
# handler for the commands /penis_size, /ps

@bot.message_handler(commands=['penis_size', 'ps'])
def handle_penis_size(message):
    name = message.from_user.username
    try:
        command, mod = message.text.split()
        size = roll_penis(int(mod))
    except Exception as e:
        print(e)
        size = roll_penis(0)
    if size[1] == 'mandingo':
        penis_size = f'Impressive, @{name}, you must be very proud\n(you rolled a {size[0]})'
    elif size[1] == 'micropenis':
        penis_size = f'Ehm... I\'m certain you have other... qualities\n(you rolled a {size[0]})'
    elif size[1] == 'weird':
        penis_size = f'Let\'s not get too negative: your boobs are pretty... nice? I guess?\n(you rolled a {size[0]})'
    else:
        penis_size = f'Yeah, you\'re normal. A  boring %.2fcm\n(you rolled a {size[0]})'%size[1]
    bot.reply_to(message, penis_size)
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


### handle_spongebob(message)
# handler for the commands /spongebob, /sp

@bot.message_handler(commands=['spongebob', 'sp'])
def handle_spongebob(message):
    try:
        output = spongebob_parser(message.text)
    except Exception as e:
        print(e)
        output = 'YoU cAn\'T eVeN sPeLl RiGht'
    bot.reply_to(message, output)
    pass

bot.polling()
