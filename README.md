# Cadastro de Clientes

Sistema de cadastro de clientes com interface gráfica em Python e banco de dados MySQL.

## 💻 Tecnologias Utilizadas

- Python 3.x
- Tkinter (interface gráfica)
- MySQL (via XAMPP)
- mysql-connector-python

## ⚙️ Funcionalidades

- Cadastrar novos clientes
- Excluir clientes cadastrados
- Listar todos os clientes
- Validação de senha

## 🛠 Como executar o projeto

1. Instale o conector do MySQL:
   ```bash
   pip install mysql-connector-python

   
CREATE DATABASE cadastro;

USE cadastro;

CREATE TABLE clientes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(50),
  sobrenome VARCHAR(50),
  cpf VARCHAR(14),
  telefone VARCHAR(20),
  senha VARCHAR(100)
);

python app.py


cadastro-clientes/
├── app.py         # Interface gráfica com Tkinter
├── database.py    # Conexão e comandos SQL
├── README.md      # Instruções do projeto
└── .gitignore     # Arquivos ignorados pelo Git

