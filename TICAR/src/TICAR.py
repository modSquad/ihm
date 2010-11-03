#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.dom.minidom import parse, parseString

dom = parse('TICAR.xml')

icar = dom.getElementsByTagName('icar')

TICAR = dict()


# Génération du TICAR



for i in icar:
    print "\\begin{center}"
    print "\\begin{tabular}{|p{5cm}|p{4cm}|p{2cm}|p{6cm}|}"
    print "\t \\hline \\textbf{Intention} & \\textbf{Contrôle} & \\textbf{Action} & \\textbf{Réponse}\\\\\\hline"

    print '\\begin{minipage}[t]{5cm}'
    for j in i.getElementsByTagName('i'):
	print j.childNodes[0].data
    print' \\end{minipage} &'
    print '\\begin{minipage}[t]{5cm}'
    for j in i.getElementsByTagName('c'):
	print j.childNodes[0].data[1:].replace('\n', '\\\\\n')
    print' \\end{minipage} &'
    for j in i.getElementsByTagName('a'):
	print j.childNodes[0].data[0:len(j.childNodes[0].data)]
    print '&'
    print '\\begin{minipage}[t]{6cm}'
    print '\\vspace{-1em}'
    for j in i.getElementsByTagName('r'):
	 print j.childNodes[0].data[0:len(j.childNodes[0].data) - 3].replace('\n','~\\\\\n~--~')
    print '\\vspace{0.5em}'
    print '\\end{minipage}'
    print '\\\\ \n \\hline'

    print "\\end{tabular}"
    print "\\end{center}"
    print ""


