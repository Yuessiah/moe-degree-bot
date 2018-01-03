#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
i2v_path = "./illustration2vec/"
sys.path.append(i2v_path)
import i2v
import PIL
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

illust2vec = None


def Start(bot, update):
    text = "I'm Moe°-bot, I can calculate how much degrees of moe from your pictures."
    bot.send_message(chat_id=update.message.chat_id, text=text)


def Receive_and_reply(bot, update):
    global top_score
    chat_id = update.message.chat_id

    img = bot.get_file(update.message.photo[-1].file_id)
    img.download(str(chat_id) + ".jpg")

    moe = PIL.Image.open(str(chat_id) + ".jpg")
    result = illust2vec.estimate_plausible_tags([moe], threshold=0.5)

    total = 0
    text = "I see the moe picture have:\n"
    for e in result[0]["general"]:
        text += e[0] + ", " + str(e[1]) + '\n'
        total += e[1]
    text += "\nand the total degree of moe is " + str(total)
    text += '!' if total >= 10 else '.'
    if total is 0: text = "Your picture is not moe."

    bot.send_message(chat_id=chat_id, text=text)

    if total >= top_score:
        img.download("Top1moe.jpg")
        top_score = total


def Feedback(bot, update):
    text = "Please send issue to https://github.com/Yuessiah/moe-degree-bot/issues"
    bot.send_message(chat_id=update.message.chat_id, text=text)


def Top1moe(bot, update):
    bot.send_photo(chat_id=update.message.chat_id, photo=open("Top1moe.jpg", "rb"))


def main():
    global illust2vec, top_score
    illust2vec = i2v.make_i2v_with_chainer(i2v_path+"illust2vec_tag_ver200.caffemodel", i2v_path+"tag_list.json")
    top_score = 0

    updater = Updater(token="478026540:AAEyHqkOBnBZhtVQPNJk6IuSnhzZzXnujAA")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.photo, Receive_and_reply))
    dispatcher.add_handler(CommandHandler("start", Start))
    dispatcher.add_handler(CommandHandler("feedback", Feedback))
    dispatcher.add_handler(CommandHandler("top1moe", Top1moe))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
