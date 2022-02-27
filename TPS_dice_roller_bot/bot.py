#! /usr/bin/python

import json
import sys

import telebot

from core import *

### TODO:
# background help
# character formation

### config
# reads the correct token from config.json

config = json.load(open('../config.json'))
if config[sys.argv[1]]:
    bot = telebot.TeleBot(token=config[sys.argv[1]])
else:
    print("###################################################")
    print("# Please setup the needed keys in the config file #")
    print("###################################################")
    sys.exit()


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
        # user_id = message.from_user.id
        # print(message)
        result, result_list, comment = roll_message(message.text)
        if comment is None or comment == '':
            response = f'@{name} rolled <b>{result}</b>, ({result_list})'
        else:
            response = f'@{name} rolled <b>{comment}</b>\n<b>{result}</b> ({result_list})'
    except Exception as e:
        # print(e)
        response = choice(SALTY_ANSWER)
    bot.reply_to(message, response, parse_mode='HTML')
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


### handle_pelor(message)
# answers to messages containing "pelor" with the right sticker

# @bot.message_handler(regexp="pelor")
# def handle_pelor(message):
#    chat_id = message.chat.id
#    bot.send_sticker(chat_id, "CAACAgQAAxkBAANDXuZB7Nb-rImmxXLfiWVXqj2OG5UAAjwAAy_0Wg-jNOhAndo8mxoE")
#    pass


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
        chat_id = message.chat.id
        message_id = message.message_id
        bot.reply_to(message, sentence)
        bot.delete_message(chat_id, message_id)
    except Exception as e:
        print(e)
        sentence = 'YoU CaN\'t eVeN SpElL RiGhT'
    pass


### handle_spongebob_reply(message)
# handler for the commands /spongerep, /spr

@bot.message_handler(commands=['spongerep', 'spr'])
def handle_spongebob_reply(message):
    try:
        sentence = spongebob_sentence_flow_decider(message)
        chat_id = message.chat.id
        message_id = message.message_id
        bot.reply_to(message.reply_to_message, sentence)
        bot.delete_message(chat_id, message_id)
    except Exception as e:
        print(e)
        sentence = 'YoU CaN\'t eVeN SpElL RiGhT'
    pass


### handle_zalgo(message)
# handler for the commands /zalgo, /z

@bot.message_handler(commands=['zalgo', 'z'])
def handle_zalgo(message):
    try:
        chat_id = message.chat.id
        message_id = message.message_id
        sentence = zalgo_sentence(message.text)
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, sentence)
    except Exception as e:
        print(e)
    pass


### handle_character_creator(message)
# handler for the command /character, /char

@bot.message_handler(commands=['character', 'char'])
def handle_character_creator(message):
    bot.reply_to(message, pg_creation_feature(), parse_mode='HTML')
    pass


bot.polling()
