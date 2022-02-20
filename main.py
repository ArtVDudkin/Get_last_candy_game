from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from game import *
from commands import *


def hi_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


with open('token.txt', 'r') as file:
    token_ = file.readline()
updater = Updater(token_)

updater.dispatcher.add_handler(CommandHandler('game', new_game))

updater.dispatcher.add_handler(CommandHandler('rules', show_rules))

updater.dispatcher.add_handler(CommandHandler('help', help_command))

print('start server')

updater.start_polling()
updater.idle()
