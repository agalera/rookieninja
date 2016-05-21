from sys import argv
import imp
import os

glob = {'realpath': os.path.split(os.path.realpath(__file__))[0]}

if len(argv) < 3:
    print "try again: python server.py -2 configfile"
    exit()

print os.path.join(os.getcwd(), argv[2])
try:
    m = imp.load_source("*", os.path.join(os.getcwd(), argv[2]))
except:
    print "file config not found"
    exit()
try:
    attrlist = m.__all__
except AttributeError:
    attrlist = dir(m)
for attr in attrlist:
    globals()[attr] = getattr(m, attr)
