from rookieninja.modules.db import Mongo


f = open('scripts/all_systems.csv', 'rb')

for line in f.readlines():
    tmp = line.split(';')
    clean_datas = []
    for x in tmp:
        x = x.replace("\r\n", "")
        clean_datas.append(x[1:])
    # Format
    clean_datas[1] = int(clean_datas[1])
    clean_datas[4] = int(clean_datas[4])
    clean_datas[5] = int(clean_datas[5])
    clean_datas[2] = clean_datas[2].split(' ')
    keys = ['system', 'class', 'static', 'star', 'planet',
            'moon', 'effect', 'region', 'constellation']
    result = {}
    for pos in range(len(keys)):
        result[keys[pos]] = clean_datas[pos]
    Mongo.wormholes.insert_one(result)
print "migrate ok"
