from rookieninja.views.fleet import fleets
from time import time, sleep
from threading import Thread
timeout = 10 * 60  # 10 minutes


def loop():
    while True:
        try:
            remove_fleets = []
            t = int(time())
            for key_fleet in fleets:
                if t > int(fleets[key_fleet]['last_update']) + timeout:
                    remove_fleets.append(key_fleet)
                    continue
                remove_players = []
                for key_player in fleets[key_fleet]['players']:
                    if t > int(fleets[key_fleet]['players'][key_player]['last_update']) + timeout:
                        remove_players.append(key_player)
                for key_player in remove_players:
                    del fleets[key_fleet]['players'][key_player]

            for key_fleet in remove_fleets:
                del fleets[key_fleet]
        except Exception, ex:
            print ex
        sleep(timeout)

t = Thread(target=loop)
t.daemon = True
t.start()
print "[active] clean ram routines!"
