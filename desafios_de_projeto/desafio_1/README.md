<div align="center">
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">
  <h1>🌍 Tradutor Multifuncional</h1>
  <p>Uma solução poderosa de tradução combinando Azure OpenAI e Azure Translator</p>
  <img src="https://img.shields.io/badge/Python-3.12+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Streamlit-1.39.0+-red.svg" alt="Streamlit Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">
</div>

## 📁 Estrutura do Projeto
```bash

desafio_1/
├── data/               # Dados do projeto
├── img/               # Imagens utilizadas
├── notebook/          # Notebooks de desenvolvimento
├── src/               # Código fonte
│   └── app.py         # Aplicação principal
├── Dockerfile         # Configuração do container
├── docker-compose.yml # Configuração do Docker Compose
├── requirements.txt   # Dependências do projeto
└── README.md         # Este arquivo
```
## 📑 Índice

- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [📑 Índice](#-índice)
- [📋 Sobre o Projeto](#-sobre-o-projeto)
  - [🎯 Tradutor de Artigos](#-tradutor-de-artigos)
  - [📄 Tradutor de Documentos](#-tradutor-de-documentos)
- [🚀 Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [📦 Requisitos](#-requisitos)
- [⚙️ Instalação e Execução](#️-instalação-e-execução)
  - [💻 Execução Local com Poetry](#-execução-local-com-poetry)
  - [🐳 Execução com Docker](#-execução-com-docker)
- [🎯 Conclusão e Aprendizados](#-conclusão-e-aprendizados)
  - [🚀 Próximos Passos:](#-próximos-passos)

## 📋 Sobre o Projeto
[🔝 Voltar ao índice](#-índice)

O Tradutor Multifuncional é uma aplicação web que oferece duas ferramentas de tradução integradas em uma única plataforma. Desenvolvida com foco na experiência do usuário, a solução atende diferentes necessidades de tradução em um ambiente profissional e intuitivo.

### 🎯 Tradutor de Artigos
[🔝 Voltar ao índice](#-índice)

O módulo de tradução de artigos utiliza a avançada API do Azure OpenAI GPT-4o mini para oferecer traduções precisas e contextualmente relevantes de artigos web. Características principais:

- Extração automática de conteúdo de URLs
- Preservação da formatação markdown
- Suporte a múltiplos idiomas
- Download do arquivo traduzido
- Interface intuitiva e responsiva

### 📄 Tradutor de Documentos
[🔝 Voltar ao índice](#-índice)

O módulo de tradução de documentos é alimentado pela Azure Translator API, oferecendo tradução profissional de documentos Word. Destaques:

- Suporte a arquivos .docx
- Múltiplos pares de idiomas
- Preservação da formatação do documento
- Download do arquivo traduzido
- Interface amigável para upload de arquivos

## 🚀 Tecnologias Utilizadas
[🔝 Voltar ao índice](#-índice)

**Core:**
- Python 3.12+
- Streamlit 1.39.0+
- Azure OpenAI
- Azure Translator

**Bibliotecas Principais:**
- `streamlit-lottie`: Animações interativas
- `python-docx`: Manipulação de documentos Word
- `beautifulsoup4`: Extração de conteúdo web
- `python-dotenv`: Gerenciamento de variáveis de ambiente

## 📦 Requisitos
[🔝 Voltar ao índice](#-índice)

- Python 3.12 ou superior
- Poetry para gerenciamento de dependências
- Conta Azure com acesso às APIs: 
  - Azure OpenAI
  - Azure Translator
  - `Fiz um tutorial com o passo a passo que pode ser acessado aqui:` [passo a passo](https://github.com/Jcnok/Bootcamp-Microsoft-Certification-Challenge--1-AI_102/tree/master/desafios_de_projeto/desafio_1/notebook#passo-a-passo-detalhado-para-o-desenvolvimento-do-projeto-de-tradu%C3%A7%C3%A3o-de-artigos-t%C3%A9cnicos-com-azure-ai)
- Docker (opcional)

## ⚙️ Instalação e Execução

### 💻 Execução Local com Poetry
[🔝 Voltar ao índice](#-índice)

1. Clone o repositório:
```bash
git clone https://github.com/Jcnok/Bootcamp-Microsoft-Certification-Challenge--1-AI_102.git

```
2. Navegue até a pasta do repositório:
```bash	
cd Bootcamp-Microsoft-Certification-Challenge--1-AI_102
```

3. Instale o Poetry (caso não tenha):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

4. Configure o ambiente virtual e instale as dependências:
```bash
poetry install
```

5. Configure as variáveis de ambiente:
```bash
cp .env.example .env
```

6. Edite o arquivo `.env` com suas credenciais:
```env
AZURE_OPENAI_KEY=sua_chave_openai
AZURE_ENDPOINT=seu_endpoint_openai
TRANSLATOR_API_KEY=sua_chave_translator
TRANSLATOR_ENDPOINT=seu_endpoint_translator
TRANSLATOR_LOCATION=sua_localizacao_translator
```

6. Execute a aplicação:
```bash
poetry run streamlit run desafios_de_projeto/desafio_1/src/app.py
```
7. Local URL: http://localhost:8501
   

### 🐳 Execução com Docker
[🔝 Voltar ao índice](#-índice)

1. Acesse a pasta onde o arquivo `Dockerfile` está localizado:
```bash
cd desafios_de_projeto/desafio_1/ 
```
2. Execute o comando:
```bash
docker-compose up --build
```

3. Acesse o app: 
-  http://localhost:8501

4. Parar a aplicação: 
```bash
docker-compose down
```

[🔝 Voltar ao índice](#-índice)


## 🎯 Conclusão e Aprendizados
[🔝 Voltar ao índice](#-índice)

Durante o desenvolvimento deste projeto, enfrei o desafio de criar uma solução que não apenas traduzisse conteúdo, mas o fizesse de maneira inteligente e contextual. A jornada me levou a explorar diferentes APIs da Azure e integrar múltiplas tecnologias em uma única aplicação coesa.




### 🚀 Próximos Passos:

Planejamos expandir o projeto com:
- Suporte a mais formatos de documento
- Análise de sentimento do texto traduzido
- Interface API REST para integrações
- Painel de analytics para métricas de uso

Este projeto não é apenas uma ferramenta de tradução, mas um exemplo de como tecnologias modernas podem ser combinadas para criar soluções empresariais robustas e escaláveis.

---

<div align="center">
  <p>Desenvolvido por Julio Okuda com ❤️ e ☕</p>
  <p>
    <a href="https://www.linkedin.com/in/juliookuda/">LinkedIn</a> •
    <a href="https://github.com/Jcnok">GitHub</a>
  </p>
</div>