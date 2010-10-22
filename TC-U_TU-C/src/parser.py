#!/usr/bin/env python

from xml.dom.minidom import parse, parseString

dom = parse('data.xml')

users = dom.getElementsByTagName('user')
commands = dom.getElementsByTagName('command')


TCU = dict()

for i in commands:
	#create the keys in the dict
	for j in i.getAttribute('uid').split(','):
		if j not in TCU:
			TCU[j] = list()

	TCU[j].append(i.childNodes[0].nodeValue)

print '\\begin{tabular}{|l|c|c|}'
print 'Profil utilsateur & DF & Liste des commandes\\\\'

mod = 0
temp = str()
header = 0


for i in TCU.keys():
    print i,' & DF & '
    header = 1
    for j in TCU[i]:
	print  '& ',j

print '\\end{tabular}'
