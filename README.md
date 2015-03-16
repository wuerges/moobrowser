
Este script baixa todas as submissoes da atividade cujo nome inicia com o texto ATT001, da ultima edicao da disciplina com codigo GEX002.
O script organiza os arquivos numa estrutura de diretorios com a seguinte hierarquia:

[Semestre]/[Disciplina]/[Atividade]/[Aluno]/[Submissoes]


Um exemplo de execucao e' este:

$ python2 moodlecmd.py -l [login] -p [password] -s 2015-1 -c GEX002 -a ATT001


O login e password devem ser preenchidos de acordo com seu usuario. 

O -s e' opcional. 
Ele e' apenas usado para criar uma pasta raiz, onde vao ser criadas todas as outras pastas. 

O -c e' o codigo da disciplina. Se uma disciplina tiver sido ofertada mais de uma vez pelo mesmo professor, ele vai procurar os arquivos na edicao mais recente.

O -a e' usado para procurar a Atividade para qual os alunos submeteram seus arquivos. E' recomendado colocar codigos unicos no comeco do nome de cada atividade para facilitar a busca por atividades. 


