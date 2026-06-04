# Sistema de Login em Python

##  Descrição do Projeto

O Sistema de Login é um projeto desenvolvido em Python com integração ao MySQL, com o objetivo de praticar conceitos de CRUD (Create, Read, Update e Delete), manipulação de banco de dados e desenvolvimento backend.

O sistema permite o gerenciamento de usuários cadastrados em um banco de dados, servindo como base para futuros projetos de autenticação e gerenciamento de contas.

---

## Funcionalidades do Projeto

###  - Implementadas

* Conexão com banco de dados MySQL
* Consulta de usuários cadastrados
* Verificação de nomes de usuários existentes
* Cadastro de novos usuários
* Estrutura inicial para operações CRUD

### - Em Desenvolvimento

* Sistema completo de login
* Atualização de dados do usuário
* Exclusão de usuários
* Validação de e-mail
* Validação de senha
* Criptografia de senhas (Hash)

---

##        Testes de Software

### Testes Realizados

#### Teste de Banco de Dados

* Verificação da conexão com MySQL.
* Consulta dos registros armazenados.

#### Teste de Cadastro

* Validação para impedir usuários duplicados.
* Inserção de novos registros.
* Atualização dos dados do usuário registrado

#### Teste de Funcionamento

* Leitura correta dos dados armazenados.
* Exibição dos usuários cadastrados.

### Evidências

Exemplo atual da tabela:

| ID | NomeUsuario         | SenhaUsuario | Email                                                             |
| -- | ------------------- | ------------ | ----------------------------------------------------------------- |
| 1  | Dyego Alves Peixoto | ********     | DyegoprocuraEstagio@Estagio.2026                                  |
| 2  | Maria               | ********     | [maria192luciana@hotmail.com](mailto:maria192luciana@hotmail.com) |

---

##    Tecnologias Utilizadas

* Python 3.12
* MySQL
* Git
* GitHub
* Linux Ubuntu

---

##   Bibliotecas Utilizadas

### Python

* mysql-connector-python

Instalação:

```bash
pip install mysql-connector-python
```

---

##           Pré-requisitos

Antes de executar o projeto, é necessário possuir:

* Python 3.12+
* MySQL Server
* Git
* Ambiente Virtual

---

##

---

## Estrutura do Banco de Dados

Tabela: Usuario

| Campo        | Tipo             |
| ------------ | ---------------- |
| id           | INT, AI , PK     |
| NomeUsuario  | VARCHAR , UNIQUE |
| SenhaUsuario | VARCHAR          |
| Email        | VARCHAR          |

---
##  Script de Criação do Banco

```sql
CREATE DATABASE SistemadeLogin;

USE SistemadeLogin;

CREATE TABLE Usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    NomeUsuario VARCHAR(100) UNIQUE NOT NULL,
    SenhaUsuario VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL
);


## Roadmap

Próximas funcionalidades:

* [ ] Login de usuários
* [ ] Atualização de dados
* [ ] Exclusão de contas
* [ ] Validação de e-mail

---

##   Autor

Desenvolvido por Dyego Alves Peixoto.

Projeto criado com fins de estudo e desenvolvimento profissional em Python, MySQL e Backend.

##
