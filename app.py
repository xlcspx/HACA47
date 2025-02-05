from flask import Flask, jsonify
import sqlite3
import subprocess

app = Flask(_name_)

# Função para buscar perguntas do banco
def buscar_perguntas():
    conn = sqlite3.connect("perguntas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, pergunta, resposta FROM perguntas")
    dados = cursor.fetchall()
    conn.close()

    perguntas = [{"id": row[0], "pergunta": row[1], "resposta": row[2]} for row in dados]
    return perguntas

# Função para interagir com o Ollama
def perguntar_ollama(pergunta):
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3.2"],
            input=pergunta,  # Removido .encode("utf-8")
            capture_output=True,
            text=True,  # Garante que a entrada/saída sejam strings
            encoding="utf-8",  # Força UTF-8
            check=True
        )

        # Depuração: imprimir saída
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)

        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Erro ao executar Ollama: {e.stderr.strip()}"

@app.route('/avaliar', methods=['GET'])
def avaliar_respostas():
    perguntas = buscar_perguntas()
    resultados = []

    for pergunta in perguntas:
        resposta_ia = perguntar_ollama(pergunta["pergunta"])
        correta = resposta_ia.lower() == pergunta["resposta"].lower()

        resultados.append({
            "id": pergunta["id"],
            "pergunta": pergunta["pergunta"],
            "resposta_ia": resposta_ia,
            "resposta_correta": pergunta["resposta"],
            "correta": correta
        })

    return jsonify(resultados)

@app.route('/')
def home():
    return "<h1>API está rodando!</h1><p>Acesse <a href='/avaliar'>/avaliar</a> para ver as avaliações.</p>"

if _name_ == '_main_':
    app.run(debug=True)
