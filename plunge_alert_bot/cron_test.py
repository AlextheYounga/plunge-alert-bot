from time import sleep
from .cron import RepeatedTimer
from random import randrange

def price(poop):
    if (poop == 'poop'):
        print('yep')
    price = randrange(4)
    print(price)
    if (price == 2):
        rt.stop()

print("starting...")
poop = 'poop'
rt = RepeatedTimer(1, price, poop) # it auto-starts, no need of rt.start()

