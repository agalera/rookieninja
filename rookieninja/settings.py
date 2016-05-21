from sys import argv
import imp
import os

if len(argv) < 3:
    print "try again: python server.py -2 configfile"
    exit()

print os.path.join(os.getcwd(), argv[2])
m = imp.load_source("*", os.path.join(os.getcwd(), argv[2]))
try:
    attrlist = m.__all__
except AttributeError:
    attrlist = dir(m)
for attr in attrlist:
    globals()[attr] = getattr(m, attr)
