# Importando SQLlite
import sqlite3 as lite

# Criando conexão
con = lite.connect('projeto.db')

# Criação das tabelas
with con:
  cur=con.cursor()
  cur.execute("CREATE TABLE aluno(id)")
