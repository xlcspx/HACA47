from flask import Flask, jsonify
import sqlite3
import subprocess

app = Flask(__name__)

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
            input=pergunta,
            capture_output=True,
            text=True,
            check=True
        )
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

if __name__ == '__main__':
    app.run(debug=True)
