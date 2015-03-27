import re


class Participante:
    def __init__(self, s):
        m = re.search(r'^([\S\s]+)\s+\((\d*)(\w*)\)$', s)
        self.nome = m.group(1)
        self.matricula = m.group(2)
        self.cargo = m.group(3)


    def e_professor(self):
        return self.cargo == "Docente"
