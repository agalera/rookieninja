import requests
from bs4 import BeautifulSoup
from rookieninja.modules.db import Mongo


def fix_keys(values):
    for x in values:
        if "-" in x:
            values[x.replace('-', '_')] = values.pop(x)


def get_external_info(Eve_Solarsystemname):
    print "indexing ...", Eve_Solarsystemname
    html = requests.get('http://evemaps.dotlan.net/system/%s' % Eve_Solarsystemname).text
    parsed_html = BeautifulSoup(html)
    result = parsed_html.body.find_all('td')
    insert = {}
    fix_pos = 0
    try:
        tmp = result[3].find_all('a')[2]
    except:
        fix_pos = 1
        tmp = result[4].find_all('a')[2]
    insert['system'] = tmp.text
    insert['region'] = tmp.attrs['href'].split('/')[2]
    insert['_id'] = tmp.attrs['class'][1].split('link-5-')[1]

    insert['planets'] = int(result[5 + fix_pos].text)
    insert['moons'] = int(result[12 + fix_pos].text)
    insert['belts'] = result[19 + fix_pos].text
    insert['constellation'] = result[17 + fix_pos].find_all('a')[2].text
    insert['security'] = result[24 + fix_pos].text
    insert['class'] = result[26 + fix_pos].text
    if "Wormhole Class" in insert['class']:
        insert['class'] = "C" + insert['class'].split("Wormhole Class ")[1]
    insert['faction'] = result[31 + fix_pos].text
    insert['local_pirates'] = result[33 + fix_pos].text
    try:
        insert['effect'] = parsed_html.find_all('h2')[7].text[24:-22]
    except:
        pass
    html = requests.get('http://www.ellatha.com/eve/WormholeSystemview.asp?key=%s' % Eve_Solarsystemname[1:]).text
    parsed_html = BeautifulSoup(html)
    for x in parsed_html.find_all('td'):
        if "wormholelistview.asp?key" in str(x):
            new_static = {}
            insert['static'] = x.text.strip().split(' ')
            for static in insert['static']:
                info = "C" + Mongo.wormholes_types.find_one({'_id': static})
                new_static[static] = info['name']
            insert['static'] = new_static
            break
    Mongo.wormholes.insert_one(insert)
    return insert
