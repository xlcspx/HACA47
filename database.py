import sqlite3

# Conecta ao banco (ou cria um novo)
conn = sqlite3.connect("perguntas.db")
cursor = conn.cursor()

# Cria a tabela para armazenar perguntas e respostas
cursor.execute('''
CREATE TABLE IF NOT EXISTS perguntas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pergunta TEXT NOT NULL,
    resposta TEXT NOT NULL
)
''')

# Lê as perguntas do JSON e insere no banco
import json

with open("simples.json", "r", encoding="utf-8") as file:
    perguntas = json.load(file)

for pergunta in perguntas:
    cursor.execute("INSERT INTO perguntas (pergunta, resposta) VALUES (?, ?)", 
                   (pergunta["pergunta"], pergunta["resposta"]))

conn.commit()
conn.close()

print("Banco de dados criado com sucesso!")
