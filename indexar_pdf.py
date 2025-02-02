import chromadb
from chromadb.utils import embedding_functions
from PyPDF2 import PdfReader

# Carregar o PDF e extrair texto
def extrair_texto_pdf(caminho_pdf):
    leitor = PdfReader(caminho_pdf)
    texto = ""
    for pagina in leitor.pages:
        texto += pagina.extract_text() + "\n"
    return texto

# Criar um banco vetorial com ChromaDB
def criar_banco_vetorial(texto):
    chroma_client = chromadb.PersistentClient(path="./banco_vetorial")
    collection = chroma_client.get_or_create_collection(name="meu_rag", 
        embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction("all-MiniLM-L6-v2"))

    # Quebrar o texto em partes menores
    partes = [texto[i:i+500] for i in range(0, len(texto), 500)]
    
    # Adicionar os dados ao banco vetorial
    for i, parte in enumerate(partes):
        collection.add(ids=[str(i)], documents=[parte])
    
    print("Banco vetorial criado com sucesso!")

# Caminho do PDF (substitua pelo nome do seu arquivo)
caminho_pdf = "teste.pdf"

# Executar o fluxo
texto_extraido = extrair_texto_pdf(caminho_pdf)
criar_banco_vetorial(texto_extraido)
