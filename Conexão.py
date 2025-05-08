import sqlite3 as db
from sqlite3 import *

def conectar_banco():
    try:
        conn = db.connect("sistemaescolar.db")
        return conn, "Conexão bem-sucedida!"
    except Error as e:
        return None, f"Erro ao conctar: {e}"
    
def inserir_NOME(conn, NOME_aluno, TURMA):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO aluno (NOME_aluno, TURMA) VALUES(?,?)"
        cursor.execute(query,(NOME_aluno, TURMA))
        conn.commit()
        return "Nome inserido com sucesso!"
    except Error as e:
        return f"Erro ao insirir nome: {e}"
    
   
