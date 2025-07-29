from langchain_chroma.vectorstores import Chroma 
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_PATH = "database"

prompt_template = """ 
Você é um especialista no assunto e deve responder de forma precisa e formal. Sua única fonte de verdade é o contexto fornecido abaixo.

Analise o contexto e responda à pergunta do usuário. 

Antes de ver o contexto e responder a pergunta, preciso que siga as seguintes regras: 

Nunca comece falando "com base no contexto", quero que responda de forma natural sem mencionar o contexto e o banco de dados.
caso não exista uma resposta, não invente.
Sempre ajude o usuario.




**Contexto:**
{response}

**Pergunta:**
{user_question}
"""

"""
nessa parte o codigo estou pegando a pergunta do usuario e verificando se existe uma possivel resposta para 
essa pergunta no banco de dados. 

results = db.similarity_search_with_relevance_scores(user_question, k=3) 
neste trecho de codigo faz uma busca e tras as 3 repostas mais relevante com uma pontuação de 0 a 1 
"""
def load_database():
    """
    Carrega o banco de dados ChromaDB com a função de embedding apropriada.
    Esta função será chamada pelo Streamlit para inicializar o banco de dados.
    """
    # Valida se a chave da API está presente no ambiente
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("A variável de ambiente GOOGLE_API_KEY não foi encontrada.")

    # Inicializa a função de embedding do Google
    embedding_function = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    
    # Carrega o banco de dados vetorial persistido no disco
    db = Chroma(
        persist_directory=DATABASE_PATH,
        embedding_function=embedding_function
    )
    return db

def get_rag_response(db_retriever, user_question: str) -> str:
    """
    Recebe uma conexão com o banco de dados e uma pergunta, busca por informações
    relevantes e gera uma resposta usando o modelo de linguagem.
    
    Args:
        db_retriever: O objeto do banco de dados Chroma já carregado.
        user_question: A pergunta feita pelo usuário.

    Returns:
        A resposta gerada pelo modelo de linguagem como uma string.
    """
    prompt_template_str = """
    Você é um especialista no assunto e deve responder de forma precisa e formal. Sua única fonte de verdade é o contexto fornecido abaixo.

    Analise o contexto e responda à pergunta do usuário. Sempre seja educado e se esforce para responder a perguntas básicas, mas se fugir muito do assunto 
    da pergunta, a resposta será negativa.

    **Contexto:**
    {context}

    **Pergunta:**
    {user_question}
    """
    
    # Busca por documentos similares no ChromaDB, com pontuação de relevância
    results = db_retriever.similarity_search_with_relevance_scores(user_question, k=4)

    if not results or results[0][1] < 0.6:
        return "Não consegui encontrar uma resposta relevante para essa pergunta no meu banco de dados."

    # Junta o conteúdo dos documentos encontrados para formar o contexto
    context = "\n\n----\n\n".join([result[0].page_content for result in results])

    # Cria o prompt com o contexto e a pergunta do usuário
    prompt = ChatPromptTemplate.from_template(prompt_template_str)
    prompt_message = prompt.invoke({"user_question": user_question, "context": context})

    # Inicializa e invoca o modelo de linguagem
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")
    response = llm.invoke(prompt_message)

    return response.content