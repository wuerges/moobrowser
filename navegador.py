import shutil
from BeautifulSoup import BeautifulSoup
import os

import webserver

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

    def navega_tarefas(self, y, d, a):
        if self.location != "home":
            raise "Not in home page"


        req = self.br.click_link(text_regex=r'%s.*' % d)
        self.br.open(req)

        req = self.br.click_link(text_regex=r'%s.*' % a)
        self.br.open(req)

        req = self.br.click_link(text_regex=r'Ver .* tarefas enviadas')
        self.br.open(req)


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

    def participantes(self, y, d, a):
        self.navega_tarefas(y, d, a);

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


