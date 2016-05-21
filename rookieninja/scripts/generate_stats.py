from rookieninja.modules.db import Mongo
from sys import argv
from random import randint
import time


while True:
    result = {'fleets': randint(600, 800), 'players': randint(2000, 3350)}
    Mongo.stats_eve.update({'_id': int(argv[1])}, result, True)
    time.sleep(60 * 5)
