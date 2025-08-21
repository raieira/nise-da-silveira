from database import get_connection

def salvar_contato(nome, email, mensagem):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO contatos (nome, email, mensagem)
        VALUES (?, ?, ?)
    """, (nome, email, mensagem))

    conn.commit()
    conn.close()

def listar_contatos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome, email, mensagem, criado_em FROM contatos ORDER BY criado_em DESC")
    contatos = cursor.fetchall()

    conn.close()
    return contatos


def add_contato(nome, email, mensagem):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO contatos (nome, email, mensagem) VALUES (?, ?, ?)',
                   (nome, email, mensagem))
    conn.commit()
    conn.close()
