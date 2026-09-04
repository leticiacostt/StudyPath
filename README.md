# 📚 StudyPath

Aplicação desenvolvida em Python para registrar, organizar e acompanhar uma jornada de estudos.

O projeto começou como uma prática de programação e evoluiu para uma aplicação integrada a banco de dados, permitindo aplicar conceitos de **Python, SQL e PostgreSQL** em um projeto desenvolvido do zero.

## 🚀 Funcionalidades

* Adicionar estudos
* Visualizar estudos
* Editar estudos
* Remover estudos
* Identificação dos registros por ID
* Validação dos dados de entrada
* Validação de datas e horas estudadas
* Armazenamento dos dados em PostgreSQL
* Operações CRUD integradas ao banco de dados
* Exibição dos registros em tabela no terminal

## 🛠️ Tecnologias

* Python
* PostgreSQL
* SQL
* Psycopg
* python-dotenv
* Tabulate
* Git
* GitHub
* Power BI

## 🗄️ Banco de dados

O StudyPath utiliza **PostgreSQL** para armazenamento e gerenciamento dos dados.

Atualmente, o banco possui duas tabelas principais:

```text
materias
    │
    │ 1:N
    ↓
estudos
```

### `materias`

Armazena as matérias cadastradas.

* `id` — chave primária
* `nome` — nome da matéria

### `estudos`

Armazena os registros de estudos.

* `id` — chave primária
* `materia_id` — chave estrangeira relacionada a `materias`
* `assunto` — assunto estudado
* `data` — data do estudo
* `horas` — quantidade de horas estudadas

A relação entre as tabelas é **1:N (um para muitos)**: uma matéria pode possuir vários registros de estudo.

O script SQL responsável pela estrutura do banco está disponível em `sql/banco.sql` na branch `feature/postgresql`.

## 🏗️ Estrutura

```text
StudyPath/
│
├── main.py
├── funcoes.py
├── banco.py
├── powerbi/
├── README.md
└── .gitignore
```

### Responsabilidades

* `main.py` — execução da aplicação e menu principal
* `funcoes.py` — lógica da aplicação, validações e interação com o usuário
* `banco.py` — conexão com PostgreSQL e operações SQL
* `powerbi/` — arquivos relacionados às análises e visualizações dos dados

As informações sensíveis da conexão com o banco são armazenadas em variáveis de ambiente e não são enviadas para o GitHub.

## 📚 Conceitos aplicados

O projeto reúne conceitos de programação, banco de dados e análise de dados, incluindo:

* Funções e modularização
* Estruturas condicionais e de repetição
* Validação e tratamento de dados
* Tratamento de exceções
* CRUD
* SQL
* PostgreSQL
* Chaves primárias e estrangeiras
* Relacionamentos entre tabelas
* JOIN
* Integração Python + PostgreSQL
* Separação de responsabilidades
* Análise e visualização de dados
* Power BI

## 🎯 Objetivo

O StudyPath é um projeto de aprendizado contínuo criado para **praticar programação e desenvolvimento de software na prática**.

A aplicação serve como um laboratório para aplicar novos conhecimentos em Python, bancos de dados, SQL, análise de dados e outras tecnologias à medida que o projeto evolui.

## 🔮 Próximos passos

Entre as próximas evoluções planejadas estão:

* Melhorias na organização e arquitetura do código
* Novas funcionalidades para gerenciamento de matérias
* Melhorias nas consultas SQL
* Expansão do dashboard para acompanhamento dos estudos
* Integração com APIs
* Funcionalidades utilizando inteligência artificial

---

**StudyPath** — um projeto desenvolvido para aprender, praticar e evoluir. 🚀