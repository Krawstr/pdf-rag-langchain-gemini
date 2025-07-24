from langchain_chroma.vectorstores import Chroma 
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_PATH = "database"

prompt_template = """ 
Você é um especialista no assunto e deve responder de forma precisa e formal. Sua única fonte de verdade é o contexto fornecido abaixo.

Analise o contexto e responda à pergunta do usuário. Se a informação não estiver presente no contexto, afirme que você não possui dados para responder àquela pergunta. Evite especulações.

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
def process_user_query_with_rag():
    user_question = input("Digite sua pergunta: ")

    embedding_function = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.getenv("GOOGLE_API_KEY"))
    
    db = Chroma(persist_directory=DATABASE_PATH, embedding_function=embedding_function)

    results = db.similarity_search_with_relevance_scores(user_question, k=3)
    if len(results) == 0 or results[0][1] < 0.5:
        print("Não consegui encontrar uma resposta relevante para essa pergunta.")
        return

    response = "\n\n----\n\n".join([result[0].page_content for result in results])

    prompt = ChatPromptTemplate.from_template(prompt_template)
    prompt = prompt.invoke({"user_question": user_question, "response": response})

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")
    response_text = llm.invoke(prompt).content
    
    print(response_text)
    
process_user_query_with_rag()