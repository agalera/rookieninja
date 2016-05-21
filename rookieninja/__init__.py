#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rookieninja import settings
from bottle import run, static_file, get, response, hook
from views import *
from rookieninja.modules.db import Mongo
# TODO: change to settings
from rookieninja.routines import *


@hook('after_request')
def set_headers():
    methods = 'PUT, GET, POST, DELETE, OPTIONS'
    headers = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
    origin = '*'
    response.headers['Access-Control-Allow-Origin'] = origin
    response.headers['Access-Control-Allow-Methods'] = methods
    response.headers['Access-Control-Allow-Headers'] = headers


@get('/static/<path:path>')  # prefer nginx
def static(path):
    return static_file(path, root='./static')


@get('/robots.txt')
def robots():
    return static('robots.txt')


def main(*args, **kwargs):
    r = Mongo.backup_memory.find_one({'_id': settings.SERVER['port']},
                                     {'_id': False})
    if r:
        print "loaded memory"
        fleet.fleets.update(r)
        print fleet.fleets
    print "started server!"
    run(**settings.SERVER)
    print "server stopped"
    print "save memory in db"
    Mongo.backup_memory.update({'_id': settings.SERVER['port']},
                               fleet.fleets, upsert=True)
    print "save finish!"

if __name__ == "__main__":
    main()
