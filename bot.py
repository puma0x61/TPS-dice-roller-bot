#! /usr/bin/python

import telebot
from random import randint

TOKEN = '1190003676:AAErBi7Sy_a2TiDzpsqEUXd6hmhQVNR2mvI'

bot = telebot.TeleBot(TOKEN)

def roll(dice, number, mod):
    result_list = []
    for i in range(0, number):
        result_list.append(randint(1, dice))
    result = sum(result_list) + mod
    return (result, result_list)

def parse_text(text):
    command, equation = text.split()
    number, other = equation.split('d')
    try:
        dice, mod = other.split('+')
        return (int(dice), int(number), int(mod))
    except Exception as e:
        print(e)
    return (int(other), int(number), 0)

@bot.message_handler(commands=['roll', 'r'])
def handle_roll(message):
    try:
        dice, number, mod = parse_text(message.text)
        result, result_list = roll(dice, number, mod)    
        response = f'{result}, ({result_list})'
    except Exception as e:
        print(e)
        response = 'Eh?'
    bot.reply_to(message, response)

bot.polling()

