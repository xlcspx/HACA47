import sqlite3
import json
import os

# Verifica se o arquivo JSON existe
json_file = "simples.json"
if not os.path.exists(json_file):
    print(f"Erro: O arquivo {json_file} não foi encontrado!")
    exit()

# Conecta ao banco (ou cria um novo)
conn = sqlite3.connect("perguntas.db")
cursor = conn.cursor()

# Cria a tabela para armazenar perguntas e respostas
cursor.execute('''
CREATE TABLE IF NOT EXISTS perguntas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pergunta TEXT NOT NULL UNIQUE,  -- Evita perguntas duplicadas
    resposta TEXT NOT NULL
)
''')

# Lê as perguntas do JSON e insere no banco
try:
    with open(json_file, "r", encoding="utf-8") as file:
        perguntas = json.load(file)

    # Verifica se o JSON está no formato correto
    if not isinstance(perguntas, list):
        raise ValueError("O JSON deve conter uma lista de perguntas.")

    for pergunta in perguntas:
        if "pergunta" not in pergunta or "resposta" not in pergunta:
            raise ValueError("Cada item no JSON deve ter 'pergunta' e 'resposta'.")

        try:
            cursor.execute("INSERT INTO perguntas (pergunta, resposta) VALUES (?, ?)",
                           (pergunta["pergunta"], pergunta["resposta"]))
        except sqlite3.IntegrityError:
            print(f"Pergunta duplicada ignorada: {pergunta['pergunta']}")

    conn.commit()
    print("Banco de dados atualizado com sucesso!")

except json.JSONDecodeError:
    print("Erro: O arquivo JSON está mal formatado.")
except Exception as e:
    print(f"Erro inesperado: {e}")

finally:
    conn.close()
