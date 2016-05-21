from sys import argv


DYNAMIC_SYSTEMS = False
MONGODB = {'HOSTS': ['localhost'],
           'DBNAME': 'eve-info'}

DEFAULT = {'host': '0.0.0.0', 'port': 9998 - int(argv[1]),
           'debug': False, 'reloader': True}

meinheld = {'host': '0.0.0.0', 'port': 9998 - int(argv[1]),
            'server': 'meinheld', 'log': False, 'quiet': True}

SERVER = meinheld

JINJA2_CACHE = '/tmp'

