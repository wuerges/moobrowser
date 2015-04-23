import shutil
from BeautifulSoup import BeautifulSoup
import os

import model

import webserver

class ProfessorBrowser:
    def __init__(self):
        self.br = webserver.br

        self.location = None

    def initialize(self):
        self.br.open("http://professor.uffs.edu.br")


    def login(self, user, passw):
        self.br.select_form(nr=0)
        print
        self.br.form['j_username']=user
        self.br.form['j_password']=passw
        self.br.submit()

        self.br.open("https://professor.uffs.edu.br/restrito/graduacao/diario-classe/registrar-faltas.xhtml")
        self.br.select_form(nr=0)
        self.br.select_form(nr=1)
        self.br.select_form(nr=2)

        for f in self.br.forms():
            print f
        #req = self.br.click_link(text_regex=r'^Registrar Encontros e Faltas$')
        #self.br.open(req)

        soup = BeautifulSoup(self.br.response().read())
        print(soup.prettify())

class MoodleBrowser:
    def __init__(self):
        self.br = webserver.br

        self.location = None

    def initialize(self):
        self.br.open('http://moodle.uffs.edu.br')
        self.location = "login"

    def login(self, user, passw):
        if self.location == "login":
            self.br.select_form(nr=0)
            self.br.form['username']=user
            self.br.form['password']=passw
            self.br.submit()
            self.location = "home"
        else:
            raise "Not in login page"

    def navega_disciplina(self, y, d):
        if self.location != "home":
            raise "Not in home page"

        req = self.br.click_link(text_regex=r'%s.*%s.*' % (d, y))


        self.br.open(req)
        self.location = d

    def navega_participantes(self, d):
        if self.location != d:
            raise "Not in %s" % d

        req = self.br.click_link(text_regex=r'^Participantes$')
        self.br.open(req)
        self.location = d + "participantes"

    def participantes(self, y, d):
        self.navega_disciplina(y, d)
        self.navega_participantes(d)



        for l in self.br.links(text_regex=r'^Mostrar todos os \d+$'):
            req = self.br.click_link(text_regex=r'^Mostrar todos os \d+$')
            self.br.open(req)

        soup = BeautifulSoup(self.br.response().read())
        table = soup.find("table", id='participants')

        #print table.prettify()

        alunos = []

        for row in table.findAll('tr')[1:]:
            col = row.findAll('td')
            aluno = model.Participante(col[1].findAll('a')[0].text)
            alunos.append(aluno)
        return alunos


    def navega_atividates(self, d, a):
        if self.location != d:
            raise "Not in %s" % d

        req = self.br.click_link(text_regex=r'%s.*' % a)
        self.br.open(req)

        req = self.br.click_link(text_regex=r'Ver .* tarefas enviadas')
        self.br.open(req)

        self.location = a


    def navega_tarefas(self, y, d, a):
        if self.location != "home":
            raise "Not in home page"

        self.navega_disciplina(y, d)
        self.navega_atividades(d, a)

    def download_activities(self, y, d, a):
        self.navega_tarefas(y, d, a);

        semester_folder = y + '/'
        disc_folder = d + '/'
        att_folder = a + '/'

        soup = BeautifulSoup(self.br.response().read())

        table = soup.find("table", id='attempts')

        for row in table.findAll('tr')[1:]:
            col = row.findAll('td')
            aluno =  col[1].findAll('a')[0].text
            ls = col[4].findAll('a')

            for l in ls:
                dst_dir = semester_folder + disc_folder + att_folder + aluno
                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)
                dst = dst_dir + '/' + l.text
                if not os.path.exists(dst):
                    f = self.br.retrieve(l['href'])
                    shutil.copyfile(f[0], dst)

        print "Download completed"

    def old_participantes(self, y, d, a):
        self.navega_tarefas(d, a);

        semester_folder = y + '/'
        disc_folder = d + '/'
        att_folder = a + '/'

        soup = BeautifulSoup(self.br.response().read())

        table = soup.find("table", id='attempts')

        alunos = {}

        for row in table.findAll('tr')[1:]:
            col = row.findAll('td')
            aluno =  col[1].findAll('a')[0].text
            if col[4].findAll('a'):
                alunos[aluno] = 10
            else:
                alunos[aluno] = 0

        for a in sorted(alunos):
            print a, ',', str(alunos[a])


