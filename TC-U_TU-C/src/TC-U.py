#!/usr/bin/env pythn
# -*- coding: utf-8 -*-

from xml.dom.minidom import parse, parseString

dom = parse('data.xml')

users = dom.getElementsByTagName('user')
commands = dom.getElementsByTagName('command')

TCU = dict()

# Génération du TC/U
print "\\begin{tabular}{|c{11cm}|c|}"
print "\t \\textbf{Commandes} & \\textbf{Liste des utilisateurs} \\hline"

for currentCommand in commands:
	users = currentCommand.getAttribute("uid").split(',')
	command = currentCommand.childNodes[0].data
	df = currentCommand.getAttribute("df")

	for user in users:
		if user not in TCU:	TCU[user] = []
		TCU[user].append((df, command))
	    
for key in TCU:
	for t in TCU[key]:
		print "\t ", key, " & ", t[0], " & ", t[1], "\\hline \\\\"

print "\\end{tabular}"

