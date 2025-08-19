import sqlite3

DB_NAME = 'clinica.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            mensagem TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_contato(nome, email, mensagem):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO contatos (nome, email, mensagem) VALUES (?, ?, ?)',
                   (nome, email, mensagem))
    conn.commit()
    conn.close()
