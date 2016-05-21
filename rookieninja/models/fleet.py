import requests


def get_kills(Eve_Solarsystemid):
    try:
        return requests.get('https://zkillboard.com/api/kills/solarSystemID/%s/no-items' % Eve_Solarsystemid, timeout=2).json()
    except:
        return "failed"

def get_eveeye(Eve_Solarsystemname):
    return requests.get('https://eveeye.com/?opt=GKW&x=lr&system=%s' % Eve_Solarsystemname)