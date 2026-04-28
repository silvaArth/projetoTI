import sqlite3 as sql
import os

def get_base_path():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(BASE_DIR, "database.db")

def conectar():
    return sql.connect(get_base_path())

def criar_tabela():
    con = conectar()
    cursor = con.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS chamados_ti (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                setor TEXT NOT NULL,
                problema TEXT NOT NULL,
                descricao TEXT NOT NULL,
                urgencia TEXT NOT NULL,
                status TEXT NOT NULL,
                data_chamado TEXT NOT NULL)
                """)
    con.commit()
    con.close()