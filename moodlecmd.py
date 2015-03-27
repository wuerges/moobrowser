#!/usr/bin/python2

import navegador
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-g", "--grades", default=False)
parser.add_option("-d", "--download", default=True)

parser.add_option("-l", "--login")
parser.add_option("-p", "--password")
parser.add_option("-s", "--semester", default="2015/1")
parser.add_option("-c", "--course")
parser.add_option("-a", "--activity")

(options, args) = parser.parse_args()

m = navegador.MoodleBrowser()
m.initialize()

m.login(options.login, options.password)

if options.grades:
    ps = m.participantes(options.semester, options.course)

    nomes = [a.nome for a in  [p for p in ps if not p.e_professor()]]
    for n in sorted(nomes):
        print n


elif options.download:
    m.download_activities(options.semester, options.course, options.activity)




