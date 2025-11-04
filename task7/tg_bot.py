import ptbot
from functools import partial
from dotenv import load_dotenv
from pytimeparse import parse
import os


def render_progressbar(total, iteration, prefix="", suffix="", length=30, fill="█", zfill="░"):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return "{0} |{1}| {2}% {3}".format(prefix, pbar, percent, suffix)


def reply(bot, chat_id, text):
    user_time = parse(text)
    message_id = bot.send_message(chat_id, "Таймер запущен")
    bot.create_countdown(user_time, partial(notify, bot), chat_id=chat_id, message_id=message_id, user_time=user_time)


def notify(bot, secs_left, chat_id, message_id, user_time):
    actual_time = user_time - secs_left
    bar = render_progressbar(user_time, actual_time, "Осталось {} секунд!\n".format(secs_left))
    bot.update_message(chat_id, message_id, bar)
    if not secs_left:
        bot.send_message(chat_id, "Время вышло")


def main():
    load_dotenv()
    tg_token = os.environ["TG_API_TOKEN"]
    bot = ptbot.Bot(tg_token)
    bot.reply_on_message(partial(reply, bot))
    bot.run_bot()


if __name__ == "__main__":
    main()
