# 📚 StudyPath

Aplicação desenvolvida em Python para registrar, organizar e acompanhar uma jornada de estudos.

O projeto começou como uma prática de programação e está sendo evoluído gradualmente conforme novos conceitos são aprendidos.

Atualmente, o StudyPath utiliza **PostgreSQL** para armazenamento dos dados e possui integração entre Python e banco de dados.

## 🚀 Funcionalidades atuais

* Adicionar estudos
* Visualizar estudos
* Editar estudos
* Remover estudos
* Identificação dos estudos por ID
* Edição individual de matéria, assunto, data e horas
* Validação dos campos de entrada
* Validação de datas no formato DD/MM/AAAA
* Validação de horas estudadas
* Tratamento de entradas inválidas
* Armazenamento dos dados em PostgreSQL
* Exibição dos estudos em tabela no terminal
* Relacionamento entre matérias e estudos
* Operações CRUD integradas ao banco de dados

## 🛠️ Tecnologias utilizadas

* Python
* PostgreSQL
* Psycopg
* python-dotenv
* Tabulate
* Git
* GitHub

## 📁 Estrutura do projeto

```text
StudyPath/
│
├── main.py
├── funcoes.py
├── banco.py
├── README.md
├── .gitignore
└── .env
```

> O arquivo `.env` é utilizado para armazenar informações sensíveis da conexão com o banco de dados e não deve ser enviado para o GitHub.

## 🗄️ Banco de dados

O StudyPath utiliza PostgreSQL como sistema de gerenciamento de banco de dados.

O banco de dados possui atualmente duas tabelas principais:

```text
materias
    │
    │ 1:N
    ↓
estudos
```

### Tabela `materias`

Armazena as matérias cadastradas.

Principais campos:

* `id` — chave primária
* `nome` — nome da matéria

### Tabela `estudos`

Armazena os registros de estudos.

Principais campos:

* `id` — chave primária
* `materia_id` — chave estrangeira relacionada à tabela `materias`
* `assunto` — assunto estudado
* `data` — data do estudo
* `horas` — quantidade de horas estudadas

A relação entre as tabelas é de **1:N (um para muitos)**: uma matéria pode possuir vários registros de estudo.

## 📚 Conceitos praticados

Durante o desenvolvimento do projeto, estão sendo aplicados conceitos como:

* Variáveis
* Entrada e saída de dados
* Estruturas condicionais
* Estruturas de repetição
* Funções
* Módulos
* Listas
* Dicionários
* CRUD
* IDs
* Validação de dados
* Tratamento de exceções
* `try/except`
* `datetime`
* Organização e modularização de código
* SQL
* PostgreSQL
* Chave primária
* Chave estrangeira
* Relacionamento entre tabelas
* JOIN
* Integração Python + PostgreSQL
* Separação de responsabilidades

## 🏗️ Arquitetura atual

O projeto utiliza uma separação simples de responsabilidades:

```text
main.py
   ↓
funcoes.py
   ↓
banco.py
   ↓
PostgreSQL
```

* `main.py` — responsável pela execução e menu da aplicação
* `funcoes.py` — responsável pela lógica da aplicação, interação com o usuário e apresentação dos dados
* `banco.py` — responsável pela conexão com o PostgreSQL e pelas operações SQL
* PostgreSQL — responsável pelo armazenamento dos dados

## 🎯 Objetivo

O objetivo do StudyPath é servir como um projeto prático para consolidar conhecimentos de programação e desenvolvimento de software.

A ideia é evoluir o projeto gradualmente, adicionando novas funcionalidades conforme novos conhecimentos forem adquiridos.

Além de funcionar como uma aplicação, o StudyPath também serve como um laboratório para aplicar conceitos de programação, banco de dados e integração entre diferentes tecnologias em um projeto desenvolvido do zero.

## 🔮 Próximas evoluções

Algumas possibilidades para futuras versões:

* Refatoração e melhoria da organização do código
* Criação de funções reutilizáveis para validação dos dados
* Melhorias na interface do terminal
* Melhorias nas consultas SQL
* Criação de novas funcionalidades para gerenciamento de matérias
* Criação de dashboard para acompanhamento dos estudos
* Criação de roadmaps de aprendizagem
* Integração com APIs
* Recomendações de estudo
* Recomendações personalizadas utilizando inteligência artificial

## 📌 Sobre o projeto

O StudyPath é um projeto de aprendizado contínuo. Sua estrutura e funcionalidades serão modificadas e aprimoradas conforme a evolução dos conhecimentos em programação.

> O objetivo não é apenas construir o sistema, mas utilizá-lo como laboratório para aprender e aplicar novos conceitos de programação, banco de dados e desenvolvimento de software.