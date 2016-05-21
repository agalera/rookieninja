from rookieninja.modules.db import Mongo


for wormhole in Mongo.wormholes.find():
    if "Wormhole Class" in wormhole['class']:
        wormhole['class'] = "C" + wormhole['class'].split("Wormhole Class ")[1]
    if "static" in wormhole:
        print "static", wormhole['static']
        continue
        if not isinstance(wormhole['static'], list):
            continue
        new_static = {}
        for static in wormhole['static']:
            info = Mongo.wormholes_types.find_one({'_id': static})
            new_static[static] = info['name']
        wormhole['static'] = new_static
    # _id = wormhole['_id']
    # del wormhole['_id']
    # Mongo.wormholes.update({'_id': _id}, wormhole)
