import streamlit as st
import asyncio
import main_logic

@st.cache_resource
def load_components():
    """
    Carrega o banco de dados Chroma usando a função do módulo main_logic.
    O decorador @st.cache_resource do Streamlit evita recarregar os componentes
    pesados a cada interação do usuário, tornando o app muito mais rápido.
    """
    # Mantém a correção para o erro de event loop no thread do Streamlit
    asyncio.set_event_loop(asyncio.new_event_loop())
    
    try:
        db = main_logic.load_database()
        return db
    except ValueError as e:
        st.error(f"Erro de configuração: {e}")
        st.info("Verifique se você tem um arquivo .env com a sua GOOGLE_API_KEY.")
        st.stop() # Para a execução do app
    except Exception as e:
        # Para outros erros inesperados durante o carregamento
        st.error(f"Ocorreu um erro inesperado ao carregar o banco de dados: {e}")
        st.info("Verifique se você executou o script 'create_db.py' e se a pasta 'database' existe e não está vazia.")
        st.stop()

# interface
st.set_page_config(page_title="Chat com Documentos", page_icon="🤖")

st.title("🤖 Chat com seus Documentos")
st.caption("Faça uma pergunta e a IA irá respondê-la com base nos documentos PDF fornecidos.")

db = load_components()

# Inicializa o histórico da conversa no st.session_state se ele não existir
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Qual a sua dúvida?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            response = main_logic.get_rag_response(db, prompt)
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
