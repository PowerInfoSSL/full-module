#!/usr/bin/python

import os,sys

os.system('./src')

o=open('fine.txt','r')
oo=o.readlines()

ww=[]
for i in oo:
    ww.append(i[:-1])
c=0
for i in ww:
    c +=1
    print c,'-Loading %s' % i
    os.system('modprobe %s' % i)
print 'Complated'
