#! /usr/bin/python

import sys
import json
import telebot

from random import randint

from core import *

### TODO:
# tit request
# background help
# character formation


config = json.load(open('../config.json'))
if config['test_bot']:
    bot = telebot.TeleBot(token=config['test_bot'])
else:
    print ("###################################################")
    print ("# Please setup the needed keys in the config file #")
    print ("###################################################")
    sys.exit()


### welcome(message)
# sends HELP_MESSAGE

@bot.message_handler(commands=['help', 'start'])
def welcome(message):
    bot.reply_to(message, HELP_MESSAGE)
    pass


### handle_nudes(message)
# asks for nudes, sometimes

@bot.message_handler(func=lambda nudes_chance: randint(1, 1000) == 1, content_types=["text"])
def handle_nudes(message):
    bot.reply_to(message, tit_request())


### handle_roll(message)
# handler for the commands /roll, /r

@bot.message_handler(commands=['roll', 'r'])
def handle_roll(message):
    try:
        name = message.from_user.username
        dice, number, mod = parse_text(message.text)
        # parse_text returns number = '0' if there was an error
        if (number == 0):
            bot.reply_to(message, 'eh?')
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


### handle_pelor(message)
# answers to messages containing "pelor" with the right sticker

@bot.message_handler(regexp="pelor")
def handle_pelor(message):
    chat_id = message.chat.id
    bot.send_sticker(chat_id, "CAACAgQAAxkBAANDXuZB7Nb-rImmxXLfiWVXqj2OG5UAAjwAAy_0Wg-jNOhAndo8mxoE")
    pass

### handle_i_am_alive
# handler for the command /alive

@bot.message_handler(commands=['alive'])
def handle_i_am_alive(message):
    name = message.from_user.username
    new_message = alive_service()
    new_message = f'Yes, @{name}, {new_message}'
    bot.reply_to(message, new_message)


### handle_edgelord
# handler for the command /edgelord

@bot.message_handler(commands=['edgelord'])
def handle_edgelord(message):
    bot.reply_to(message, edgelord_feature())
    pass
    

### handle_spongebob(message)
# handler for the commands /spongebob, /sp

@bot.message_handler(commands=['spongebob', 'sp'])
def handle_spongebob(message):
    try:
        sentence = spongebob_sentence(message.text)
    except Exception as e:
        print(e)
        sentence = 'YoU CaN\'t eVeN SpElL RiGhT'
    bot.reply_to(message, sentence)
    pass


### handle_spongebob_reply(message)
# handler for the commands /spongebob, /sp

@bot.message_handler(commands=['spongerep', 'spr'])
def handle_spongebob_reply(message):
    try:
        sentence = spongebob_sentence(message.reply_to_message.text)
    except Exception as e:
        print(e)
        sentence = 'YoU CaN\'t eVeN SpElL RiGhT'
    bot.reply_to(message.reply_to_message, sentence)
    pass


bot.polling()

