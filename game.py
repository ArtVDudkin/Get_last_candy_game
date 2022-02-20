from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import random


def new_game(update: Update, context: CallbackContext):
    init_candys = 200
    max_candys_by_step = 28
    current_candys = init_candys
    msg = 'Привет, дорогой друг! Предлагаем сыграть в увлекательную игру "Забери последнюю конфетку!" Правила простые: ' + \
          f'на столе лежат 200 конфет. Вы по очереди берёте несколько конфет, но не более 28 штук за раз. ' + \
          f'Побеждает тот, кто заберёт последнюю конфету и не оставит ничего другому игроку!'
    update.message.reply_text(msg)
    players = []
    players.append(update.effective_user.first_name)
    bot_names = ['Василий', 'Никодим', 'Кеша', 'Вольдемар', 'Кузя', 'Яша']
    bot = 'бот ' + random.choice(bot_names)
    players.append(bot)
    update.message.reply_text(f'И сегодня против Вас играет {bot}')

    current_player_index = 1
    while current_candys > 0:
        if current_player_index == 0:
            current_player_index = 1
        else:
            current_player_index = 0
        current_candys = Next_move(current_candys, max_candys_by_step, players, current_player_index)

    if current_player_index == 0:
        update.message.reply_text(f'Ура, Вы забираете последнюю конфету! Поздравляем! Хотите, сыграем еще раз y/n?')
    else:
        update.message.reply_text(f'И последнюю конфету забирает {players[current_player_index]}! В следующий раз Вам обязательно повезёт! Хотите, сыграем еще раз y/n?')
    answer = update.message.text
    while (answer != 'y') and (answer != 'n'):
        update.message.reply_text(f'Если хотите сыграть еще раз, нажмите: y - да, n - нет')
        answer = update.message.text
    if answer == 'y':
        new_game()
    else:
        exit()
    return


def Get_new_value(update: Update, context: CallbackContext, message):
    update.message.reply_text(message)
    return update.message.text


def Show_message(update: Update, context: CallbackContext, msg):
    update.message.reply_text(msg)


def Check_step(value: str, max_candys_by_step):
    while not value.isnumeric():
        msg = f'Ошибка ввода! Введите число от 1 до {max_candys_by_step}'
        value = Get_new_value(msg)
    step = int(value)
    return step


def Next_move(current_candys, max_candys_by_step, players, current_player):
    if current_player == 0:
        msg = f'{players[current_player]}, Ваш ход! Возьмите от 1 до {max_candys_by_step} конфет. Всего конфет осталось: {current_candys}'
        value = Get_new_value(msg)
        step = Check_step(value, max_candys_by_step)

        while (step < 1) or (step > max_candys_by_step) or (step > current_candys):
            if step <= 0:
                msg = f'{players[current_player]}, количество взятых конфет должно быть больше 1!'
            if step > max_candys_by_step:
                msg = f'{players[current_player]}, не более {max_candys_by_step} конфет!'
            if step > current_candys:
                msg = f'{players[current_player]}, конфет осталось всего {current_candys}! Вы не можете взять больше! Попробуйте еще раз?'
            value = Get_new_value(msg)
            step = Check_step(value, max_candys_by_step)
    else:
        step = Player_bot(current_candys, max_candys_by_step)
        Show_message(f'{players[current_player]} забирает {step} конфет')
    return current_candys - step


def Player_bot(current_candys, max_candys_by_step):
    step = current_candys % (max_candys_by_step + 1)
    if step < 1:
        step = random.randint(1, max_candys_by_step)
    return step
