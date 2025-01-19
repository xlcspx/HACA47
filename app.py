from flask import Flask, jsonify
import json
import subprocess

app = Flask(__name__)

# Carrega as perguntas do arquivo JSON
with open('simples.json', 'r', encoding='utf-8') as file:
    perguntas = json.load(file)

# Função para interagir com o Ollama
def perguntar_ollama(pergunta):
    try:
        # Envia a pergunta ao Ollama usando `ollama run`
        result = subprocess.run(
            ["ollama", "run", "llama3.2"],  
            input=pergunta,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()  # Retorna a resposta do Ollama
    except subprocess.CalledProcessError as e:
        return f"Erro ao executar Ollama: {e.stderr.strip()}"

@app.route('/avaliar', methods=['GET'])
def avaliar_respostas():
    resultados = []

    for idx, pergunta in enumerate(perguntas):
        questao = pergunta["pergunta"]
        resposta_correta = pergunta["resposta"]

        # Envia a pergunta ao Ollama e captura a resposta
        resposta_ia = perguntar_ollama(questao)

        # Compara a resposta do Ollama com a resposta correta
        correta = resposta_ia.lower() == resposta_correta.lower()

        resultados.append({
            "id": idx,
            "pergunta": questao,
            "resposta_ia": resposta_ia,
            "resposta_correta": resposta_correta,
            "correta": correta
        })

    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True)
