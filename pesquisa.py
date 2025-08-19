import sqlite3

conn = sqlite3.connect("clinica.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM contatos")
for linha in cursor.fetchall():
    print(linha)

conn.close()
