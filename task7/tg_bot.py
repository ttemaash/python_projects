import ptbot
from dotenv import load_dotenv
from pytimeparse import parse
import os
import random
import sys


load_dotenv()


TG_TOKEN = os.environ["TG_API_TOKEN"]
bot = ptbot.Bot(TG_TOKEN)


def render_progressbar(total, iteration, prefix="", suffix="", length=30, fill="█", zfill="░"):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return "{0} |{1}| {2}% {3}".format(prefix, pbar, percent, suffix)


def reply(chat_id, text):
    user_time = parse(text)
    bar = render_progressbar(user_time, 0, "Осталось {} секунд!\n".format(user_time))
    message_id = bot.send_message(chat_id, bar)
    bot.create_countdown(user_time, notify, chat_id=chat_id, message_id=message_id, user_time=user_time)


def notify(secs_left, chat_id, message_id, user_time):
    actual_time = user_time - secs_left
    bar = render_progressbar(user_time, actual_time, "Осталось {} секунд!\n".format(actual_time))
    bot.update_message(chat_id, message_id, bar)
    if not secs_left:
        bot.send_message(chat_id, "Время вышло")


def main():
    bot.reply_on_message(reply)
    bot.run_bot()


if __name__ == "__main__":
    main()
