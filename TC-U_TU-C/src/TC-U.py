#!/usr/bin/env pythn
# -*- coding: utf-8 -*-

from xml.dom.minidom import parse, parseString

dom = parse('data.xml')

users = dom.getElementsByTagName('user')
commands = dom.getElementsByTagName('command')

TCU = dict()
Usernames = dict()

for u in users:
	    Usernames[u.getAttribute("id")] = u.childNodes[0].data

lastUser = ""
lastDF = -1

# Génération du TC/U
print "\\begin{center}"
print "\\begin{tabular}{|c|c|c|}"
print "\t \\hline \\textbf{Utilisateur} & \\textbf{DF} & \\textbf{Liste des commandes} \\\\"

for currentCommand in commands:
	User = Usernames[currentCommand.getAttribute("uid")]
	DF = currentCommand.getAttribute("df")
	Command = currentCommand.childNodes[0].data

	if lastUser == User: User = ""
	else: lastUser = User

	if lastDF == DF: DF = ""
	else: lastDF = DF

	if User != "": print "\\hline"
	print "\t", User, "~& ", DF, "~&", Command, "\\\\ "

print "\\hline"
print "\\end{tabular}"
print "\\end{center}"

