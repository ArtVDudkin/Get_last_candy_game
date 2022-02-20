from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def show_rules(update: Update, context: CallbackContext):
    msg = 'Привет, дорогой друг! Предлагаем сыграть в увлекательную игру "Забери последнюю конфетку!" Правила простые: ' + \
          f'на столе лежат 200 конфет. Вы по очереди берёте несколько конфет, но не более 28 штук за раз. ' + \
          f'Побеждает тот, кто заберёт последнюю конфету и не оставит ничего другому игроку! Начать игру /game'
    update.message.reply_text(msg)


def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'/game\n/rules\n/help')