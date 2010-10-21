#!/usr/bin/env python

from xml.dom.minidom import parse, parseString

dom = parse('data.xml')

users = dom.getElementsByTagName('user')
commands = dom.getElementsByTagName('command')


for i in users:
	print i.getAttribute('id')

TCU = dict()

for i in commands:
	#create the keys in the dict
	for j in i.getAttribute('uid').split(','):
		if j not in TCU:
			TCU[j] = list()

	TCU[j].append(i.childNodes[0].nodeValue)

print TCU
