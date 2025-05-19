import tkinter as tk
from tkinter import messagebox
from database import inserir_cliente, buscar_clientes, excluir_cliente, criar_tabela

# Cria tabela se não existir
criar_tabela()

def cadastrar():
    if senha.get() != confirmar_senha.get():
        messagebox.showerror("Erro", "As senhas não coincidem!")
        return

    inserir_cliente(
        nome.get(),
        sobrenome.get(),
        cpf.get(),
        telefone.get(),
        senha.get()
    )
    messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
    listar()
    limpar()

def listar():
    lista.delete(0, tk.END)
    for cliente in buscar_clientes():
        lista.insert(tk.END, f"{cliente[0]} - {cliente[1]} {cliente[2]} - CPF: {cliente[3]} - Tel: {cliente[4]}")

def deletar():
    selecionado = lista.curselection()
    if selecionado:
        cliente_id = int(lista.get(selecionado).split(" - ")[0])
        excluir_cliente(cliente_id)
        listar()
    else:
        messagebox.showwarning("Atenção", "Selecione um cliente para excluir.")

def limpar():
    nome.delete(0, tk.END)
    sobrenome.delete(0, tk.END)
    cpf.delete(0, tk.END)
    telefone.delete(0, tk.END)
    senha.delete(0, tk.END)
    confirmar_senha.delete(0, tk.END)

# Interface gráfica
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("500x500")

tk.Label(janela, text="Nome").pack()
nome = tk.Entry(janela)
nome.pack()

tk.Label(janela, text="Sobrenome").pack()
sobrenome = tk.Entry(janela)
sobrenome.pack()

tk.Label(janela, text="CPF").pack()
cpf = tk.Entry(janela)
cpf.pack()

tk.Label(janela, text="Telefone").pack()
telefone = tk.Entry(janela)
telefone.pack()

tk.Label(janela, text="Senha").pack()
senha = tk.Entry(janela, show="*")
senha.pack()

tk.Label(janela, text="Confirmar Senha").pack()
confirmar_senha = tk.Entry(janela, show="*")
confirmar_senha.pack()

tk.Button(janela, text="Cadastrar", command=cadastrar).pack(pady=10)
tk.Button(janela, text="Excluir Selecionado", command=deletar).pack()

lista = tk.Listbox(janela, width=80)
lista.pack(pady=20)

listar()

janela.mainloop() 

#by celinh
