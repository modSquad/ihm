#!/usr/bin/env pythn
# -*- coding: utf-8 -*-

from xml.dom.minidom import parse, parseString

dom = parse('data.xml')

users = dom.getElementsByTagName('user')
commands = dom.getElementsByTagName('command')

TCU = []
Usernames = dict()

for u in users:
	Usernames[u.getAttribute("id")] = u.childNodes[0].data

# Génération du TU/C

print "\\begin{center}"
print "\\begin{tabular}{|c|p{10cm}|}"
print "\t \\hline \\textbf{Commandes} & \\textbf{Liste des utilisateurs} \\\\ \\hline"

for currentCommand in commands:
	print "\t", currentCommand.childNodes[0].data, " & {\centering ", Usernames[currentCommand.getAttribute("uid")], "}\\\\ \\hline"

print "\\end{tabular}"
print "\\end{center}"
