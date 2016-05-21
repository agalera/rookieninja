from rookieninja.modules.db import Mongo
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm


def get_external_info(Eve_Solarsystemname):
    if Mongo.wormholes.find_one({'system': Eve_Solarsystemname}):
        return True
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

    insert['planets'] = int(result[5+fix_pos].text)
    insert['moons'] = int(result[12+fix_pos].text)
    insert['belts'] = result[19+fix_pos].text
    insert['constellation'] = result[17+fix_pos].find_all('a')[2].text
    insert['security'] = result[24+fix_pos].text
    insert['class'] = result[26+fix_pos].text
    insert['faction'] = result[31+fix_pos].text
    insert['local_pirates'] = result[33+fix_pos].text
    try:
        insert['effect'] = parsed_html.find_all('h2')[7].text[24:-22]
    except:
        pass
    html = requests.get('http://www.ellatha.com/eve/WormholeSystemview.asp?key=%s' % Eve_Solarsystemname[1:]).text
    parsed_html = BeautifulSoup(html)
    for x in parsed_html.find_all('td'):
        if "wormholelistview.asp?key" in str(x):
            insert['static'] = x.text.strip().split(' ')
            break
    Mongo.wormholes.insert_one(insert)
    return insert

f = open('force_index.txt', 'rb')
systems = []
x = f.readline()[1:]
for y in x.split('),('):
    systems.append(y.split(',')[3][1:-1])

for system in tqdm(systems, maxinterval=1):
    try:
        get_external_info(system)
    except:
        print "system error", system
