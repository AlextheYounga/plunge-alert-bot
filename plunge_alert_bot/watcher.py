from bs4 import BeautifulSoup
import requests
import sched
import time
from time import sleep
from .cron import RepeatedTimer
from telegram.ext import Updater
from telegram.ext import CommandHandler
from .key import TOKEN
import logging
from random import randrange


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="This bot will alert you if the market crashes")

    # HTTP request to check the price of the S&P 500 from WSJ
    def priceCheck(headers, url):
        # r = requests.get(url, headers=headers)
        # print('Checked S&P price')
        # soup = BeautifulSoup(r.text,'html.parser')
        # price = soup.select_one("span#quote_val").text

        # Random number generator to show functionality.
        price = randrange(4)
        print(price)
        if (price == 2):
            context.bot.send_message(chat_id=update.effective_chat.id, text="The market has crashed")
            rt.stop()
            updater.stop()

    print("starting cron...")
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = 'https://www.wsj.com/market-data/quotes/index/SPX'
    rt = RepeatedTimer(10, priceCheck, headers, url)
    # integer here determines how many seconds the cron 'beeps' and at what pace it runs the priceCheck function.


# Telegram updater functions
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)  # logging not set up yet
updater = Updater(token=TOKEN, use_context=True)
# handlers for Telegram-recipient initiated commands, such as /start
start_handler = CommandHandler('start', start)
dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)

# Keeps the bot running
updater.start_polling()
