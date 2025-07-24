<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerador de README.md para Emergia-RAG</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        .markdown-body {
            box-sizing: border-box;
            min-width: 200px;
            max-width: 980px;
            margin: 0 auto;
            padding: 45px;
        }
        .markdown-body h1 { font-size: 2em; font-weight: 600; border-bottom: 1px solid #d0d7de; padding-bottom: .3em; }
        .markdown-body h2 { font-size: 1.5em; font-weight: 600; border-bottom: 1px solid #d0d7de; padding-bottom: .3em; margin-top: 24px; }
        .markdown-body h3 { font-size: 1.25em; font-weight: 600; margin-top: 24px; }
        .markdown-body p, .markdown-body ul, .markdown-body ol { margin-top: 16px; margin-bottom: 16px; }
        .markdown-body ul { list-style-type: disc; padding-left: 2em; }
        .markdown-body li { margin-top: .25em; }
        .markdown-body code { font-family: monospace; background-color: rgba(209, 213, 219, 0.4); padding: .2em .4em; margin: 0; font-size: 85%; border-radius: 6px; }
        .markdown-body pre { background-color: #f6f8fa; padding: 16px; border-radius: 6px; overflow: auto; }
        .markdown-body pre code { background-color: transparent; padding: 0; }
        .markdown-body blockquote { padding: 0 1em; color: #57606a; border-left: .25em solid #d0d7de; }
        .markdown-body img { max-width: 100%; }
    </style>
</head>
<body class="bg-gray-100 text-gray-800">

    <div class="container mx-auto p-4 md:p-8">
        <div class="bg-white rounded-xl shadow-lg overflow-hidden">
            <div class="p-6 md:p-8 border-b border-gray-200">
                <h1 class="text-2xl md:text-3xl font-bold text-gray-900">README para o Projeto Emergia-RAG</h1>
                <p class="mt-2 text-gray-600">Use os botões abaixo para copiar o código Markdown ou baixar o ficheiro `README.md` diretamente.</p>
            </div>

            <div class="p-6 md:p-8 flex flex-col sm:flex-row gap-4">
                <button id="copy-button" class="w-full sm:w-auto flex-1 bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg transition-transform transform hover:scale-105 focus:outline-none focus:ring-4 focus:ring-blue-300">
                    Copiar Texto Markdown
                </button>
                <button id="download-button" class="w-full sm:w-auto flex-1 bg-green-600 hover:bg-green-700 text-white font-bold py-3 px-6 rounded-lg transition-transform transform hover:scale-105 focus:outline-none focus:ring-4 focus:ring-green-300">
                    Baixar README.md
                </button>
            </div>
            
            <div id="toast" class="hidden fixed bottom-10 right-10 bg-gray-900 text-white py-2 px-4 rounded-lg shadow-xl transition-opacity duration-300">
                Texto copiado com sucesso!
            </div>

            <!-- Pré-visualização do README -->
            <div class="p-6 md:p-8 border-t border-gray-200">
                <h2 class="text-xl md:text-2xl font-bold text-gray-900 mb-4">Pré-visualização</h2>
                <div class="markdown-body bg-gray-50 p-4 rounded-lg border border-gray-200">
                    <h1>Emergia-RAG: Sistema de Perguntas e Respostas com IA</h1>
                    <p>
                        <img src="https://img.shields.io/badge/Python-3.9%2B-blue.svg" alt="Python">
                        <img src="https://img.shields.io/badge/Framework-LangChain-green.svg" alt="Framework">
                        <img src="https://img.shields.io/badge/LLM-Gemini_API-red.svg" alt="LLM">
                        <img src="https://img.shields.io/badge/Vector_DB-ChromaDB-purple.svg" alt="Database">
                    </p>
                    <hr>
                    <h2>📜 Índice</h2>
                    <ul>
                        <li><a href="#-1-motivação">1. Motivação</a></li>
                        <li><a href="#-2-o-que-é-emergia">2. O que é Emergia?</a></li>
                        <li><a href="#-3-arquitetura-do-sistema-rag">3. Arquitetura do Sistema (RAG)</a></li>
                        <li><a href="#-4-como-funciona">4. Como Funciona</a></li>
                        <li><a href="#-5-stack-de-tecnologias">5. Stack de Tecnologias</a></li>
                        <li><a href="#-6-configuração-do-ambiente">6. Configuração do Ambiente</a></li>
                        <li><a href="#-7-como-usar">7. Como Usar</a></li>
                        <li><a href="#-8-desafios-e-soluções">8. Desafios e Soluções</a></li>
                        <li><a href="#-9-próximos-passos">9. Próximos Passos</a></li>
                        <li><a href="#-10-agradecimentos">10. Agradecimentos</a></li>
                    </ul>
                    <hr>
                    <h2 id="-1-motivação">💡 1. Motivação</h2>
                    <p>Tudo começou com um "erro de digitação" no meu currículo, apontado pelo meu mentor durante uma conversa. A palavra era <strong>"emergia"</strong>, e não "energia". Expliquei que o termo estava correto e se referia a um conceito fascinante da ecologia, frequentemente desconhecido.</p>
                    <p>Essa confusão me inspirou a transformar a curiosidade em um projeto prático. Unindo a sugestão do meu mentor de explorar agentes de IA com meu interesse no tema, decidi construir um sistema focado exclusivamente em responder perguntas sobre Emergia, garantindo que as respostas fossem precisas e confiáveis.</p>
                    
                    <h2 id="-2-o-que-é-emergia">🌿 2. O que é Emergia?</h2>
                    <p><strong>Emergia</strong> (do inglês, <em>emergy</em> ou <em>embodied energy</em>) é um conceito da ecologia e da termodinâmica que se refere à quantidade total de energia de um determinado tipo (geralmente solar) que foi utilizada, direta ou indiretamente, para gerar um produto, serviço ou recurso. É uma forma de avaliar o verdadeiro "custo" ambiental e energético de algo, considerando toda a cadeia de transformações na natureza e na economia.</p>
                    
                    <h2 id="-3-arquitetura-do-sistema-rag">🏗️ 3. Arquitetura do Sistema (RAG)</h2>
                    <p>Este projeto implementa o padrão de arquitetura <strong>Retrieval-Augmented Generation (RAG)</strong>. O objetivo do RAG é aprimorar a qualidade das respostas de Modelos de Linguagem Grandes (LLMs), tornando-as mais confiáveis e menos propensas a "alucinações" (informações factualmente incorretas).</p>
                    <p>O fluxo funciona da seguinte forma:</p>
                    <pre><code>Pergunta do Usuário -&gt; [1. Recuperação de Documentos] -&gt; [2. Injeção de Contexto no Prompt] -&gt; [3. Geração de Resposta pelo LLM] -&gt; Resposta Final
</code></pre>
                    <p>Em vez de enviar a pergunta diretamente ao LLM, o sistema primeiro busca em uma base de conhecimento privada (neste caso, artigos e PDFs sobre Emergia) os trechos mais relevantes. Esses trechos são então fornecidos ao LLM como um contexto, para que ele formule uma resposta baseada nos fatos apresentados.</p>
                    
                    <h2 id="-4-como-funciona">🛠️ 4. Como Funciona</h2>
                    <h3>Etapa 1: Indexação de Dados (Offline)</h3>
                    <p>Esta etapa prepara a base de conhecimento que alimentará o sistema. É executada uma única vez ou sempre que a base de dados for atualizada. O script responsável por esta fase é o <code>create_db.py</code>.</p>
                    <ol>
                        <li><strong>Carregamento de Dados (<code>Data Loading</code>)</strong>: Documentos em formato PDF, localizados em um diretório, são carregados utilizando a classe <code>PyPDFDirectoryLoader</code> do LangChain.</li>
                        <li><strong>Segmentação de Documentos (<code>Chunking</code>)</strong>: Os documentos são divididos em segmentos menores (<em>chunks</em>) usando <code>RecursiveCharacterTextSplitter</code>. Esta técnica, a mais recomendada, tenta manter a coesão semântica do texto ao dividi-lo em separadores lógicos.</li>
                        <li><strong>Geração de Embeddings (<code>Embedding Generation</code>)</strong>: Cada <em>chunk</em> de texto é convertido em um vetor numérico de alta dimensão usando o modelo <code>models/embedding-001</code> da API do Google.</li>
                        <li><strong>Armazenamento e Indexação (<code>Vector Storage & Indexing</code>)</strong>: Os vetores de embedding, juntamente com os textos originais, são armazenados em um banco de dados vetorial local, o <strong>ChromaDB</strong>.</li>
                    </ol>
                    <h3>Etapa 2: Inferência e Geração (Online)</h3>
                    <p>Esta etapa ocorre em tempo real a cada pergunta do usuário e é gerenciada pelo script <code>main.py</code>.</p>
                    <ol>
                        <li><strong>Consulta do Usuário</strong>: O sistema recebe uma pergunta sobre Emergia.</li>
                        <li><strong>Vetorização da Consulta</strong>: A pergunta é convertida em um vetor de embedding usando o mesmo modelo da Etapa 1.</li>
                        <li><strong>Busca por Similaridade</strong>: O sistema realiza uma busca no ChromaDB para encontrar os <em>k</em> chunks de texto mais similares à pergunta.</li>
                        <li><strong>Aumento do Prompt</strong>: Os <em>chunks</em> recuperados são inseridos em um template de prompt juntamente com a pergunta original, instruindo o LLM a responder com base <em>exclusivamente</em> no contexto fornecido.</li>
                        <li><strong>Geração da Resposta</strong>: O prompt aumentado é enviado ao LLM (API do Gemini), que sintetiza uma resposta coesa e factual.</li>
                    </ol>

                    <h2 id="-5-stack-de-tecnologias">🚀 5. Stack de Tecnologias</h2>
                    <ul>
                        <li><strong>Linguagem</strong>: Python</li>
                        <li><strong>Orquestração de LLMs</strong>: LangChain</li>
                        <li><strong>Modelo de Linguagem (LLM)</strong>: Google Gemini API</li>
                        <li><strong>Modelo de Embedding</strong>: Google <code>models/embedding-001</code></li>
                        <li><strong>Banco de Dados Vetorial</strong>: ChromaDB</li>
                        <li><strong>Manipulação de Dados</strong>: <code>PyPDFDirectoryLoader</code>, <code>RecursiveCharacterTextSplitter</code></li>
                    </ul>

                    <h2 id="-6-configuração-do-ambiente">⚙️ 6. Configuração do Ambiente</h2>
                    <ol>
                        <li><strong>Clone o repositório:</strong><pre><code>git clone https://github.com/seu-usuario/emergia-rag.git
cd emergia-rag</code></pre></li>
                        <li><strong>Crie e ative um ambiente virtual:</strong><pre><code># Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
.\\venv\\Scripts\\activate</code></pre></li>
                        <li><strong>Instale as dependências:</strong><pre><code>pip install -r requirements.txt</code></pre></li>
                        <li><strong>Configure suas credenciais:</strong><br>Crie um ficheiro <code>.env</code> na raiz do projeto e adicione a sua chave da API do Google:<pre><code>GOOGLE_API_KEY="SUA_CHAVE_API_AQUI"</code></pre></li>
                    </ol>

                    <h2 id="-7-como-usar">▶️ 7. Como Usar</h2>
                    <ol>
                        <li><strong>Prepare a Base de Conhecimento:</strong>
                            <ul>
                                <li>Crie uma pasta chamada <code>data</code> na raiz do projeto.</li>
                                <li>Adicione todos os seus ficheiros PDF sobre Emergia dentro desta pasta.</li>
                            </ul>
                        </li>
                        <li><strong>Execute o script de indexação:</strong><pre><code>python create_db.py</code></pre></li>
                        <li><strong>Execute a interface de consulta:</strong><pre><code>python main.py</code></pre></li>
                    </ol>

                    <h2 id="-8-desafios-e-soluções">🧠 8. Desafios e Soluções</h2>
                    <p>O principal desafio técnico foi lidar com o limite de requisições da API do Google (<code>erro 429 Too Many Requests</code>) ao tentar vetorizar centenas de <em>chunks</em> de uma só vez.</p>
                    <p><strong>Solução:</strong> Implementei um sistema de processamento em lotes (<em>batch processing</em>). Em vez de enviar todos os <em>chunks</em> de uma vez, o código agrupa-os em lotes de tamanho 100. O primeiro lote é usado para criar o banco de dados, e os lotes subsequentes são adicionados num loop. Para garantir a robustez, adicionei uma pausa de 1 segundo (<code>time.sleep(1)</code>) entre o processamento de cada lote.</p>

                    <h2 id="-9-próximos-passos">🎯 9. Próximos Passos</h2>
                    <ul>
                        <li>[ ] <strong>Aprimorar a Base de Dados</strong>: Realizar uma curadoria mais rigorosa dos artigos e buscar mais fontes.</li>
                        <li>[ ] <strong>Desenvolver uma Interface Gráfica</strong>: Criar uma GUI com <code>Tkinter</code> ou uma interface web com <code>Flask</code>/<code>Django</code>.</li>
                        <li>[ ] <strong>Refinar a Recuperação</strong>: Implementar técnicas mais avançadas de recuperação para melhorar a qualidade do contexto.</li>
                        <li>[ ] <strong>Avaliação do Sistema</strong>: Criar um conjunto de dados de perguntas e respostas para avaliar objetivamente a performance do RAG.</li>
                    </ul>

                    <h2 id="-10-agradecimentos">🙏 10. Agradecimentos</h2>
                    <p>Um agradecimento especial ao meu mentor, cuja provocação inicial foi o catalisador para este projeto. O aprendizado foi imenso.</p>
                    <p>Feedbacks e contribuições são sempre bem-vindos!</p>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Conteúdo Markdown para ser copiado e baixado
        const markdownContent = `# Emergia-RAG: Sistema de Perguntas e Respostas com IA

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Framework](https://img.shields.io/badge/Framework-LangChain-green.svg)
![LLM](https://img.shields.io/badge/LLM-Gemini_API-red.svg)
![Database](https://img.shields.io/badge/Vector_DB-ChromaDB-purple.svg)

---

## 📜 Índice

* [1. Motivação](#-1-motivação)
* [2. O que é Emergia?](#-2-o-que-é-emergia)
* [3. Arquitetura do Sistema (RAG)](#-3-arquitetura-do-sistema-rag)
* [4. Como Funciona](#-4-como-funciona)
    * [Etapa 1: Indexação de Dados (Offline)](#etapa-1-indexação-de-dados-offline)
    * [Etapa 2: Inferência e Geração (Online)](#etapa-2-inferência-e-geração-online)
* [5. Stack de Tecnologias](#-5-stack-de-tecnologias)
* [6. Configuração do Ambiente](#-6-configuração-do-ambiente)
* [7. Como Usar](#-7-como-usar)
* [8. Desafios e Soluções](#-8-desafios-e-soluções)
* [9. Próximos Passos](#-9-próximos-passos)
* [10. Agradecimentos](#-10-agradecimentos)

---

## 💡 1. Motivação

Tudo começou com um "erro de digitação" no meu currículo, apontado pelo meu mentor durante uma conversa. A palavra era **"emergia"**, e não "energia". Expliquei que o termo estava correto e se referia a um conceito fascinante da ecologia, frequentemente desconhecido.

Essa confusão me inspirou a transformar a curiosidade em um projeto prático. Unindo a sugestão do meu mentor de explorar agentes de IA com meu interesse no tema, decidi construir um sistema focado exclusivamente em responder perguntas sobre Emergia, garantindo que as respostas fossem precisas e confiáveis.

## 🌿 2. O que é Emergia?

**Emergia** (do inglês, *emergy* ou *embodied energy*) é um conceito da ecologia e da termodinâmica que se refere à quantidade total de energia de um determinado tipo (geralmente solar) que foi utilizada, direta ou indiretamente, para gerar um produto, serviço ou recurso. É uma forma de avaliar o verdadeiro "custo" ambiental e energético de algo, considerando toda a cadeia de transformações na natureza e na economia.

## 🏗️ 3. Arquitetura do Sistema (RAG)

Este projeto implementa o padrão de arquitetura **Retrieval-Augmented Generation (RAG)**. O objetivo do RAG é aprimorar a qualidade das respostas de Modelos de Linguagem Grandes (LLMs), tornando-as mais confiáveis e menos propensas a "alucinações" (informações factualmente incorretas).

O fluxo funciona da seguinte forma:

\`\`\`
Pergunta do Usuário -> [1. Recuperação de Documentos] -> [2. Injeção de Contexto no Prompt] -> [3. Geração de Resposta pelo LLM] -> Resposta Final
\`\`\`

Em vez de enviar a pergunta diretamente ao LLM, o sistema primeiro busca em uma base de conhecimento privada (neste caso, artigos e PDFs sobre Emergia) os trechos mais relevantes. Esses trechos são então fornecidos ao LLM como um contexto, para que ele formule uma resposta baseada nos fatos apresentados.

## 🛠️ 4. Como Funciona

### Etapa 1: Indexação de Dados (Offline)

Esta etapa prepara a base de conhecimento que alimentará o sistema. É executada uma única vez ou sempre que a base de dados for atualizada. O script responsável por esta fase é o \`create_db.py\`.

1.  **Carregamento de Dados (\`Data Loading\`)**: Documentos em formato PDF, localizados em um diretório, são carregados utilizando a classe \`PyPDFDirectoryLoader\` do LangChain.
2.  **Segmentação de Documentos (\`Chunking\`)**: Os documentos são divididos em segmentos menores (*chunks*) usando \`RecursiveCharacterTextSplitter\`. Esta técnica, a mais recomendada, tenta manter a coesão semântica do texto ao dividi-lo em separadores lógicos.
3.  **Geração de Embeddings (\`Embedding Generation\`)**: Cada *chunk* de texto é convertido em um vetor numérico de alta dimensão usando o modelo \`models/embedding-001\` da API do Google.
4.  **Armazenamento e Indexação (\`Vector Storage & Indexing\`)**: Os vetores de embedding, juntamente com os textos originais, são armazenados em um banco de dados vetorial local, o **ChromaDB**.

### Etapa 2: Inferência e Geração (Online)

Esta etapa ocorre em tempo real a cada pergunta do usuário e é gerenciada pelo script \`main.py\`.

1.  **Consulta do Usuário**: O sistema recebe uma pergunta sobre Emergia.
2.  **Vetorização da Consulta**: A pergunta é convertida em um vetor de embedding usando o mesmo modelo da Etapa 1.
3.  **Busca por Similaridade**: O sistema realiza uma busca no ChromaDB para encontrar os *k* chunks de texto mais similares à pergunta.
4.  **Aumento do Prompt**: Os *chunks* recuperados são inseridos em um template de prompt juntamente com a pergunta original, instruindo o LLM a responder com base *exclusivamente* no contexto fornecido.
5.  **Geração da Resposta**: O prompt aumentado é enviado ao LLM (API do Gemini), que sintetiza uma resposta coesa e factual.

## 🚀 5. Stack de Tecnologias

* **Linguagem**: Python
* **Orquestração de LLMs**: LangChain
* **Modelo de Linguagem (LLM)**: Google Gemini API
* **Modelo de Embedding**: Google \`models/embedding-001\`
* **Banco de Dados Vetorial**: ChromaDB
* **Manipulação de Dados**: \`PyPDFDirectoryLoader\`, \`RecursiveCharacterTextSplitter\`

## ⚙️ 6. Configuração do Ambiente

1.  **Clone o repositório:**
    \`\`\`bash
    git clone https://github.com/seu-usuario/emergia-rag.git
    cd emergia-rag
    \`\`\`

2.  **Crie e ative um ambiente virtual:**
    \`\`\`bash
    # Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # Windows
    python -m venv venv
    .\\venv\\Scripts\\activate
    \`\`\`

3.  **Instale as dependências:**
    (Crie um ficheiro \`requirements.txt\` com as bibliotecas necessárias, como \`langchain\`, \`google-generativeai\`, \`chromadb\`, \`pypdf\`, etc.)
    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`

4.  **Configure suas credenciais:**
    Crie um ficheiro \`.env\` na raiz do projeto e adicione sua chave da API do Google:
    \`\`\`
    GOOGLE_API_KEY="SUA_CHAVE_API_AQUI"
    \`\`\`

## ▶️ 7. Como Usar

1.  **Prepare a Base de Conhecimento:**
    * Crie uma pasta chamada \`data\` na raiz do projeto.
    * Adicione todos os seus ficheiros PDF sobre Emergia dentro desta pasta.

2.  **Execute o script de indexação:**
    Este script irá processar os PDFs, gerar os embeddings e criar o banco de dados vetorial.
    \`\`\`bash
    python create_db.py
    \`\`\`

3.  **Execute a interface de consulta:**
    Após a criação do banco, execute o script principal para começar a fazer perguntas.
    \`\`\`bash
    python main.py
    \`\`\`
    O terminal irá exibir um prompt para você digitar sua pergunta.

## 🧠 8. Desafios e Soluções

O principal desafio técnico foi lidar com o limite de requisições da API do Google (\`erro 429 Too Many Requests\`) ao tentar vetorizar centenas de *chunks* de uma só vez.

**Solução:** Implementei um sistema de processamento em lotes (*batch processing*). Em vez de enviar todos os *chunks* de uma vez, o código os agrupa em lotes de tamanho 100. O primeiro lote é usado para criar o banco de dados, e os lotes subsequentes são adicionados num loop. Para garantir a robustez, adicionei uma pausa de 1 segundo (\`time.sleep(1)\`) entre o processamento de cada lote, evitando exceder a cota de requisições por minuto da API.

## 🎯 9. Próximos Passos

Este projeto foi uma excelente introdução à arquitetura RAG. As melhorias planejadas incluem:

* [ ] **Aprimorar a Base de Dados**: Realizar uma curadoria mais rigorosa dos artigos e buscar mais fontes.
* [ ] **Desenvolver uma Interface Gráfica**: Criar uma GUI com \`Tkinter\` ou uma interface web com \`Flask\`/\`Django\`.
* [ ] **Refinar a Recuperação**: Implementar técnicas mais avançadas de recuperação para melhorar a qualidade do contexto.
* [ ] **Avaliação do Sistema**: Criar um conjunto de dados de perguntas e respostas para avaliar objetivamente a performance do RAG.

## 🙏 10. Agradecimentos

Um agradecimento especial ao meu mentor, cuja provocação inicial foi o catalisador para este projeto. O aprendizado foi imenso.

Feedbacks e contribuições são sempre bem-vindos!`;

        const copyButton = document.getElementById('copy-button');
        const downloadButton = document.getElementById('download-button');
        const toast = document.getElementById('toast');

        // Função para copiar
        copyButton.addEventListener('click', () => {
            // Usa a API Clipboard para maior compatibilidade e segurança
            navigator.clipboard.writeText(markdownContent).then(() => {
                // Mostra a notificação (toast)
                toast.classList.remove('hidden');
                toast.classList.add('opacity-100');
                setTimeout(() => {
                    toast.classList.remove('opacity-100');
                    toast.classList.add('hidden');
                }, 2000);
            }).catch(err => {
                console.error('Erro ao copiar texto: ', err);
                alert('Não foi possível copiar o texto. Por favor, tente manualmente.');
            });
        });

        // Função para baixar
        downloadButton.addEventListener('click', () => {
            const blob = new Blob([markdownContent], { type: 'text/markdown;charset=utf-8' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'README.md';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        });
    </script>

</body>
</html>
