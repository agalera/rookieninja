import pymongo
from rookieninja.settings import MONGODB


Mongo = pymongo.MongoClient(host=MONGODB['HOSTS'],
                            connect=False)[MONGODB['DBNAME']]
