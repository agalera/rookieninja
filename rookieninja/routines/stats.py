from rookieninja.views.fleet import fleets
from time import sleep
from threading import Thread
from rookieninja.modules.db import Mongo
from sys import argv
timeout = 10 * 60  # 10 minutes


def loop():
    while True:
        sleep(30)
        result = {'fleets': len(fleets), 'players': 0}
        for key_fleet in fleets:
            result['players'] += len(fleets[key_fleet].get('players', []))
        Mongo.stats_eve.update({'_id': int(argv[1])}, result, True)
        sleep(timeout - 30)

t = Thread(target=loop)
t.daemon = True
t.start()
print "[active] stats routines!"
