
---

## **2️⃣ database.py atualizado**

```python
import sqlite3

def criar_conexao():
    conn = sqlite3.connect('clinica.db')
    return conn

def criar_tabelas():
    conn = criar_conexao()
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        telefone TEXT
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS atendimentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER,
        data TEXT,
        descricao TEXT,
        FOREIGN KEY(paciente_id) REFERENCES pacientes(id)
    )
    """)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    criar_tabelas()
    print("Banco de dados e tabelas criados com sucesso!")
