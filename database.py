import sqlite3

def conectar():
    return sqlite3.connect("clientes.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            sobrenome TEXT,
            cpf TEXT,
            telefone TEXT,
            senha TEXT
        )
    """)
    conn.commit()
    conn.close()

def inserir_cliente(nome, sobrenome, cpf, telefone, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nome, sobrenome, cpf, telefone, senha) VALUES (?, ?, ?, ?, ?)",
                   (nome, sobrenome, cpf, telefone, senha))
    conn.commit()
    conn.close()

def buscar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    return clientes

def excluir_cliente(cliente_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))
    conn.commit()
    conn.close()

#bycelinh

