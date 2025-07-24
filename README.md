Emergia-RAG: Sistema de Perguntas e Respostas com IA
Um sistema de Perguntas e Respostas focado no conceito de Emergia, construído com uma arquitetura de Geração Aumentada por Recuperação (RAG) para fornecer respostas precisas e baseadas em fontes especializadas.

📜 Índice
1. Motivação

2. O que é Emergia?

3. Arquitetura do Sistema (RAG)

4. Como Funciona

Etapa 1: Indexação de Dados (Offline)

Etapa 2: Inferência e Geração (Online)

5. Stack de Tecnologias

6. Configuração do Ambiente

7. Como Usar

8. Desafios e Soluções

9. Próximos Passos

10. Agradecimentos

💡 1. Motivação
Tudo começou com um "erro de digitação" no meu currículo, apontado pelo meu mentor durante uma conversa. A palavra era "emergia", e não "energia". Expliquei que o termo estava correto e se referia a um conceito fascinante da ecologia, frequentemente desconhecido.

Essa confusão me inspirou a transformar a curiosidade em um projeto prático. Unindo a sugestão do meu mentor de explorar agentes de IA com meu interesse no tema, decidi construir um sistema focado exclusivamente em responder perguntas sobre Emergia, garantindo que as respostas fossem precisas e confiáveis.

🌿 2. O que é Emergia?
Emergia (do inglês, emergy ou embodied energy) é um conceito da ecologia e da termodinâmica que se refere à quantidade total de energia de um determinado tipo (geralmente solar) que foi utilizada, direta ou indiretamente, para gerar um produto, serviço ou recurso. É uma forma de avaliar o verdadeiro "custo" ambiental e energético de algo, considerando toda a cadeia de transformações na natureza e na economia.

🏗️ 3. Arquitetura do Sistema (RAG)
Este projeto implementa o padrão de arquitetura Retrieval-Augmented Generation (RAG). O objetivo do RAG é aprimorar a qualidade das respostas de Modelos de Linguagem Grandes (LLMs), tornando-as mais confiáveis e menos propensas a "alucinações" (informações factualmente incorretas).

O fluxo funciona da seguinte forma:

Pergunta do Usuário -> [1. Recuperação de Documentos] -> [2. Injeção de Contexto no Prompt] -> [3. Geração de Resposta pelo LLM] -> Resposta Final

Em vez de enviar a pergunta diretamente ao LLM, o sistema primeiro busca em uma base de conhecimento privada (neste caso, artigos e PDFs sobre Emergia) os trechos mais relevantes. Esses trechos são então fornecidos ao LLM como um contexto, para que ele formule uma resposta baseada nos fatos apresentados.

🛠️ 4. Como Funciona
O processo é dividido em duas fases principais:

Etapa 1: Indexação de Dados (Offline)
Esta etapa prepara a base de conhecimento que alimentará o sistema. É executada uma única vez ou sempre que a base de dados for atualizada. O script responsável por esta fase é o create_db.py.

Carregamento de Dados (Data Loading): Documentos em formato PDF, localizados em um diretório, são carregados utilizando a classe PyPDFDirectoryLoader do LangChain.

Segmentação de Documentos (Chunking): Os documentos são divididos em segmentos menores (chunks) usando RecursiveCharacterTextSplitter. Esta técnica, a mais recomendada, tenta manter a coesão semântica do texto ao dividi-lo em separadores lógicos.

Geração de Embeddings (Embedding Generation): Cada chunk de texto é convertido em um vetor numérico de alta dimensão usando o modelo models/embedding-001 da API do Google.

Armazenamento e Indexação (Vector Storage & Indexing): Os vetores de embedding, juntamente com os textos originais, são armazenados em um banco de dados vetorial local, o ChromaDB.

Etapa 2: Inferência e Geração (Online)
Esta etapa ocorre em tempo real a cada pergunta do usuário e é gerenciada pelo script main.py.

Consulta do Usuário: O sistema recebe uma pergunta sobre Emergia.

Vetorização da Consulta: A pergunta é convertida em um vetor de embedding usando o mesmo modelo da Etapa 1.

Busca por Similaridade: O sistema realiza uma busca no ChromaDB para encontrar os k chunks de texto mais similares à pergunta.

Aumento do Prompt: Os chunks recuperados são inseridos em um template de prompt juntamente com a pergunta original, instruindo o LLM a responder com base exclusivamente no contexto fornecido.

Geração da Resposta: O prompt aumentado é enviado ao LLM (API do Gemini), que sintetiza uma resposta coesa e factual.

🚀 5. Stack de Tecnologias
Linguagem: Python

Orquestração de LLMs: LangChain

Modelo de Linguagem (LLM): Google Gemini API

Modelo de Embedding: Google models/embedding-001

Banco de Dados Vetorial: ChromaDB

Manipulação de Dados: PyPDFDirectoryLoader, RecursiveCharacterTextSplitter

⚙️ 6. Configuração do Ambiente
Clone o repositório:

git clone https://github.com/seu-usuario/emergia-rag.git
cd emergia-rag

Crie e ative um ambiente virtual:

# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
.\venv\Scripts\activate

Instale as dependências:
(Crie um arquivo requirements.txt com as bibliotecas necessárias, como langchain, google-generativeai, chromadb, pypdf, etc.)

pip install -r requirements.txt

Configure suas credenciais:
Crie um arquivo .env na raiz do projeto e adicione sua chave da API do Google:

GOOGLE_API_KEY="SUA_CHAVE_API_AQUI"

▶️ 7. Como Usar
Prepare a Base de Conhecimento:

Crie uma pasta chamada data na raiz do projeto.

Adicione todos os seus arquivos PDF sobre Emergia dentro desta pasta.

Execute o script de indexação:
Este script irá processar os PDFs, gerar os embeddings e criar o banco de dados vetorial.

python create_db.py

Execute a interface de consulta:
Após a criação do banco, execute o script principal para começar a fazer perguntas.

python main.py

O terminal irá exibir um prompt para você digitar sua pergunta.

🧠 8. Desafios e Soluções
O principal desafio técnico foi lidar com o limite de requisições da API do Google (erro 429 Too Many Requests) ao tentar vetorizar centenas de chunks de uma só vez.

Solução: Implementei um sistema de processamento em lotes (batch processing). Em vez de enviar todos os chunks de uma vez, o código os agrupa em lotes de tamanho 100. O primeiro lote é usado para criar o banco de dados, e os lotes subsequentes são adicionados em um loop. Para garantir a robustez, adicionei uma pausa de 1 segundo (time.sleep(1)) entre o processamento de cada lote, evitando exceder a cota de requisições por minuto da API.

🎯 9. Próximos Passos
Este projeto foi uma excelente introdução à arquitetura RAG. As melhorias planejadas incluem:

[ ] Aprimorar a Base de Dados: Realizar uma curadoria mais rigorosa dos artigos e buscar mais fontes.

[ ] Desenvolver uma Interface Gráfica: Criar uma GUI com Tkinter ou uma interface web com Flask/Django para tornar o sistema mais amigável.

[ ] Refinar a Recuperação: Implementar técnicas mais avançadas de recuperação para melhorar a qualidade do contexto.

[ ] Avaliação do Sistema: Criar um conjunto de dados de perguntas e respostas para avaliar objetivamente a performance do RAG.

🙏 10. Agradecimentos
Um agradecimento especial ao meu mentor, cuja provocação inicial foi o catalisador para este projeto. O aprendizado foi imenso.

Feedbacks e contribuições são sempre bem-vindos!
