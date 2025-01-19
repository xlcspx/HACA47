import json

perguntas = [
    {"pergunta": "Os Objetivos de Desenvolvimento Sustentável (ODS) foram adotados pela ONU em 2015?", "resposta": "Verdadeiro"},
    {"pergunta": "Existem 20 ODS estabelecidos pela ONU", "resposta": "Falso"},
    {"pergunta": "O ODS 1 visa erradicar a pobreza em todas as suas formas", "resposta": "Verdadeiro"},
    {"pergunta": "O ODS 5 promove a igualdade de gênero", "resposta": "Verdadeiro"},
    {"pergunta": "Os ODS não abordam questões relacionadas à mudança climática", "resposta": "Falso"},
    {"pergunta": "O ODS 14 trata da vida terrestre", "resposta": "Falso"},
    {"pergunta": "A educação de qualidade é o foco do ODS 4", "resposta": "Verdadeiro"},
    {"pergunta": "Os ODS são obrigatórios para todos os países membros da ONU", "resposta": "Falso"},
    {"pergunta": "O ODS 7 busca assegurar o acesso à energia limpa e acessível", "resposta": "Verdadeiro"},
    {"pergunta": "O ODS 10 visa reduzir as desigualdades dentro e entre os países", "resposta": "Verdadeiro"},
    {"pergunta": "Os ODS não incluem metas relacionadas à saúde pública", "resposta": "Falso"},
    {"pergunta": "O ODS 11 foca em tornar as cidades e comunidades sustentáveis", "resposta": "Verdadeiro"},
    {"pergunta": "A parceria global para o desenvolvimento sustentável é o objetivo do ODS 17", "resposta": "Verdadeiro"},
    {"pergunta": "Os ODS substituíram os Objetivos de Desenvolvimento do Milênio (ODM)", "resposta": "Verdadeiro"}
  

 ]
# Usa ensure_ascii=False para manter os caracteres UTF-8
object_json = json.dumps(perguntas, indent=4, ensure_ascii=False)

with open("simples.json", "w", encoding="utf-8") as file:
    file.write(object_json)
