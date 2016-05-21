from bottle import get, request, redirect
from rookieninja.modules.utils import fix_keys, get_external_info
from rookieninja.modules.db import Mongo
from rookieninja.modules.draw import template
from rookieninja import settings
import uuid
from time import time
import sys


#simulate_request = {'Eve-Charid': '91562314', 'Accept-Language': 'en-us,en', 'Eve-Shipname': '? Free transport', 'Content-Length': '', 'Accept-Charset': 'iso-8859-1,*,utf-8', 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0 EVE-IGB', 'Eve-Solarsystemid': '31000007', 'Eve-Regionid': '10000002', 'Eve-Trusted': 'Yes', 'Eve-Shiptypeid': '34317', 'Host': '95.122.82.245:9999', 'Eve-Charname': 'Admirallo', 'Eve-Solarsystemname': 'J105443', 'Eve-Corpid': '98456577', 'Accept-Encoding': 'gzip,deflate', 'Cache-Control': 'max-age=0', 'Eve-Shiptypename': 'Confessor', 'Eve-Serverip': '87.237.34.200:26000', 'Connection': 'keep-alive', 'Eve-Regionname': 'The Forge', 'Eve-Stationname': 'Niyabainen IV - Moon 1 - Caldari Navy Assembly Plant', 'Content-Type': 'text/plain', 'Eve-Constellationname': 'Kimotoro', 'Accept': 'application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5', 'Eve-Constellationid': '20000020', 'Eve-Corpname': 'Anonimos Multiservis', 'Eve-Stationid': '60003769', 'Eve-Shipid': '1021005433030'}
fleets = {}


@get('/<server>/update/<fleet>/<system>')
def update(server, fleet, system):
    # values = simulate_request
    values = dict(request.headers)
    fix_keys(values)
    require_reload = False
    data = {}

    if 'Eve_Solarsystemid' in values:
        if values['Eve_Solarsystemname'] != system:
            require_reload = True
        if len(values['Eve_Solarsystemname']) == 7 and values['Eve_Solarsystemname'][0] == "J":
            data['Eve_wh'] = values['Eve_Solarsystemname']
        else:
            data['Eve_Solarsystemname'] = values['Eve_Solarsystemname']
            data['Eve_Solarsystemid'] = values['Eve_Solarsystemid']
            data['Eve_wh'] = None

        data['Eve_Charname'] = values['Eve_Charname']
        data['Eve_Shiptypeid'] = values['Eve_Shiptypeid']
        data['Eve_Shiptypename'] = values['Eve_Shiptypename']
        data['Eve_Shipname'] = values['Eve_Shipname']
        data['last_update'] = int(time())

        try:
            fleets[fleet]['players'][values['Eve_Charid']].update(data)
        except:
            try:
                fleets[fleet]['players'][values['Eve_Charid']] = data
            except:
                fleets[fleet] = {'players': {values['Eve_Charid']: data}}
    try:
        fleets[fleet]['last_update'] = int(time())
        result = fleets[fleet]
        result['reload'] = require_reload
        return result
    except:
        return None


@get('/<server>/fleet/<fleet>')
def fleet(server, fleet):
    # values = simulate_request
    values = dict(request.headers)
    fix_keys(values)
    trusted = True
    if 'Eve_Solarsystemid' not in values:
        trusted = False
        values = {'Eve_Solarsystemname': 'Jita'}
    # values = dict(request.headers)
    return info(values['Eve_Solarsystemname'],
                trusted, fleet, server)


@get('/create_fleet')
def create_fleet():
    return redirect("/%s/fleet/%s" % (sys.argv[1], str(uuid.uuid4())))


@get('/system/<Eve_Solarsystemname>/<server>')
def info(Eve_Solarsystemname, trusted=False, fleet=False, server=0):
    values = {'trusted': trusted, 'fleet': fleet, 'server': server}
    values['system_info'] = Mongo.wormholes.find_one({'system': Eve_Solarsystemname})
    if settings.DYNAMIC_SYSTEMS and not values['system_info']:
        try:
            values['system_info'] = get_external_info(Eve_Solarsystemname)
        except:
            return "not exists!"
    # values['kills'] = get_kills(values['system_info']['_id'])
    return template('fleet.tpl', **values)
