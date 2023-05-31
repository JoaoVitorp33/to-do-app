# Importando sqlite3
import sqlite3 as lite

# Criando e conectando com o banco de dados
con = lite.connect("lista.db")


# Inserir tarefas
def inserir(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO tarefa (nome) VALUES (?)"
        cur.execute(query, i)
        
# Selecionar tarefas
def selecionar():
    lista_tarefas = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM tarefa")
        rows = cur.fetchall()
        for row in rows:
            lista_tarefas.append(row)
    return lista_tarefas

# Deletar tarefas
def deletar(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM tarefa WHERE id=?"
        cur.execute(query, i)
        
# Atualizar tarefas
def atualizar(i):
    with con:
        cur = con.cursor()
        query = "UPDATE tarefa SET nome=? WHERE id=?"
        cur.execute(query, i)
        
        

"""# Criar tabela
with con:
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE tarefa(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")"""