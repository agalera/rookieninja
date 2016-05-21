from models.fleet import get_kills
from requests import get
from rookieninja.modules.db import Mongo
from threading import Thread


def prepare_request(kill):
    x = {'Eve-Charid': kill['characterID'], 'Eve-Shipname': '? Free transport', 'Eve-Solarsystemid': '31000007', 'Eve-Regionid': '10000002', 'Eve-Trusted': 'Yes', 'Eve-Shiptypeid': kill['shipTypeID'], 'Eve-Charname': kill['characterName'], 'Eve-Solarsystemname': 'Niyabainen', 'Eve-Corpid': '98456577', 'Eve-Regionname': 'The Forge', 'Eve-Stationname': 'Niyabainen IV - Moon 1 - Caldari Navy Assembly Plant', 'Eve-Constellationname': 'Kimotoro', 'Eve-Constellationid': '20000020', 'Eve-Corpname': 'Anonimos Multiservis', 'Eve-Stationid': '60003769', 'Eve-Shipid': '1021005433030'}

    query = Mongo.ships.find_one({'_id': kill['shipTypeID']})
    if not query:
        print("no tiene", kill['shipTypeID'])
        r = get('https://www.fuzzwork.co.uk/api/typeid.php?typeid=%s' % kill['shipTypeID']).json()
        Mongo.ships.insert({'typeName': r['typeName'], '_id': kill['shipTypeID']})
        query = {'typeName': r['typeName'], '_id': kill['shipTypeID']}
    x['Eve-Shiptypename'] = query['typeName']
    return x
players = []
kills = get_kills(30000142)
for kill in kills:
    for x in kill['attackers']:
        if x['shipTypeID'] in [0, 9965]:
            continue
        if x['characterID'] == 0:
            continue
        players.append(prepare_request(x))


def send_to_rookie(headers):
    get('http://rookie.ninja/8/update/1efef360-520e-4d27-9e92-bc52712050a0/Niyabainen',
        headers=headers)
    print "get ok"
for headers in players:
    print "enviando a rookie.ninja"
    t = Thread(target=send_to_rookie, args=(headers,)).start()
print "all threads start"
# import ipdb; ipdb.set_trace()