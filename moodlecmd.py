#!/usr/bin/python2

import navegador
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l", "--login")
parser.add_option("-p", "--password")
parser.add_option("-s", "--semester", default="2015-1")
parser.add_option("-c", "--course")
parser.add_option("-a", "--activity")

(options, args) = parser.parse_args()

m = navegador.MoodleBrowser()
m.initialize()

m.login(options.login, options.password)

m.download_activities(options.semester, options.course, options.activity)

#m.participantes('2015-1', 'GEX002', 'ATT001')



