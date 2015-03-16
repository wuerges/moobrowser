
Este script baixa todas as submissoes da atividade cujo nome inicia com o texto ATT001, da ultima edicao da disciplina com codigo GEX002.
O script organiza os arquivos numa estrutura de diretorios com a seguinte hierarquia:

<Semestre>/<Disciplina>/<Atividade>/<Aluno>/<Submissoes>


$ python2 moodlecmd.py -l <login> -p <password> -s 2015-1 -c GEX002 -a ATT001
