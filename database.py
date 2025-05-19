import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # altere se tiver senha
        database="cadastro"
    )

def inserir_cliente(nome, sobrenome, cpf, telefone, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO clientes (nome, sobrenome, cpf, telefone, senha) VALUES (%s, %s, %s, %s, %s)",
        (nome, sobrenome, cpf, telefone, senha)
    )
    conn.commit()
    conn.close()

def buscar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, sobrenome, cpf FROM clientes")
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def excluir_cliente(id_cliente):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = %s", (id_cliente,))
    conn.commit()
    conn.close()
