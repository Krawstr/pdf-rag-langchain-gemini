from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
from time import sleep

load_dotenv()

BASE_FOLDER = "base"

def create_db():
    documents = load_documents()
    chunks = split_chunks(documents)

    if chunks:
        vectorize_chunks(chunks)
    else:
        print("Nenhum documento para processar.")

def load_documents():
    print(f"Carregando documentos da pasta '{BASE_FOLDER}'...")
    loader = PyPDFDirectoryLoader(BASE_FOLDER)
    documents = loader.load()
    print(f"Foram carregados {len(documents)} documentos.")
    return documents

def split_chunks(documents):
    """
    Divide os documentos carregados em chunks menores.
    """
    if not documents:
        return []
    
    print("Dividindo documentos em chunks...")
    split_document = RecursiveCharacterTextSplitter(
        chunk_size=3000,      # Tamanho máximo de cada chunk
        chunk_overlap=200,      # Quantidade de caracteres sobrepostos entre chunks
        length_function=len,
        add_start_index=True
    )
    chunks = split_document.split_documents(documents)
    print(f"Total de {len(chunks)} chunks criados.")
    return chunks
    
def vectorize_chunks(chunks):
    """
    Cria embeddings para os chunks e os armazena no ChromaDB em lotes.
    """
    google_api_key = os.getenv("GOOGLE_API_KEY") 

    if not google_api_key:
        raise ValueError("A variável de ambiente GOOGLE_API_KEY não foi encontrada.")

    print("Inicializando o modelo de embedding do Google...")
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=google_api_key)
    
    # Tamanho do lote para evitar limites de taxa da API
    batch_size = 100 
    
    print("Criando o banco de dados Chroma com o primeiro lote...")
    # Pega o primeiro lote para criar o banco de dados inicial
    first_batch = chunks[:batch_size]
    db = Chroma.from_documents(
        documents=first_batch, 
        embedding=embeddings, 
        persist_directory="database"
    )


    for i in range(batch_size, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        
        current_batch_num = (i // batch_size) + 1
        total_batches = (len(chunks) + batch_size - 1) // batch_size
        
        print(f"Processando lote {current_batch_num} de {total_batches}...")
        
        db.add_documents(documents=batch, embedding=embeddings)
        
        sleep(1)

    print("✅ Banco de dados criado com sucesso!")

if __name__ == "__main__":
    create_db()