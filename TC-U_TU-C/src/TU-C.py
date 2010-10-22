#!/usr/bin/env pythn
# -*- coding: utf-8 -*-

from xml.dom.minidom import parse, parseString

dom = parse('data.xml')

users = dom.getElementsByTagName('user')
commands = dom.getElementsByTagName('command')

TCU = []

# Génération du TU/C

print "\\begin{tabular}{|c{11cm}|c|}"
print "\t \\textbf{Commandes} & \\textbf{Liste des utilisateurs} \\hline"

for currentCommand in commands:
	print "\t", currentCommand.getAttribute("uid"), " & ",  currentCommand.childNodes[0].data, "\\hline \\"

print "\\end{tabular}"
