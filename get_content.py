#!/usr/bin/env python
import sys
import urllib2
import memcache

url = sys.argv[1].strip()
f = urllib2.urlopen(url)
s = memcache.Client(["218.244.128.35:11212"])
#s.set(url, f.read())
s.set('test', 'hhy')
print s.get('test')

