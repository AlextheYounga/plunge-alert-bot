from bs4 import BeautifulSoup
import requests
from telegram.ext import Updater
updater = Updater(token='TOKEN', use_context=True)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url = 'https://www.wsj.com/market-data/quotes/index/SPX'
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text,'html.parser')
price = soup.select_one("span#quote_val").text
print(price)