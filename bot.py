#! /usr/bin/python

import telebot

TOKEN = '1190003676:AAErBi7Sy_a2TiDzpsqEUXd6hmhQVNR2mvI'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['roll'])
def handle_roll(message):
    bot.reply_to(message, 'you rolled a die')

bot.polling()

