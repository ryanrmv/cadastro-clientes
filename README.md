# Cadastro de Clientes (Python + SQLite)
## ✅ Funcionalidades

- Cadastrar novos clientes com os seguintes dados:
  - Nome
  - Sobrenome
  - CPF
  - Telefone
  - Senha (com confirmação)
- Listar clientes cadastrados
- Excluir clientes da lista
- Interface gráfica com Tkinter
- Banco de dados local com SQLite (sem necessidade de servidor externo)
- Compatível com geração de executável `.exe` usando PyInstaller

## 📦 Requisitos

- Python 3.8 ou superior
- Módulo `tkinter` (já incluído no Python)
- Módulo `sqlite3` (já incluído no Python)

## ▶️ Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
2.Execute o programa:
`python app.py`

🛠 Como gerar o executável (.exe)
1. Instale o PyInstaller:
`pip install pyinstaller`


2. Gere o executável:
`pyinstaller --onefile --windowed app.py`

Estrutura do Projeto

📦 projeto/
├── app.py               # Interface gráfica
├── database.py          # Funções de banco de dados (SQLite)
├── clientes.db          # Banco de dados local (gerado automaticamente)
├── README.md
├── .gitignore
└── dist/                # Executável gerado com PyInstaller


