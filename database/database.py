import sqlite3 as sql

def criar_tabela():
    con = sql.connect("database/database.db")
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