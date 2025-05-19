import tkinter as tk
from tkinter import messagebox
from database import inserir_cliente, buscar_clientes, excluir_cliente

def cadastrar():
    nome = entry_nome.get()
    sobrenome = entry_sobrenome.get()
    cpf = entry_cpf.get()
    telefone = entry_telefone.get()
    senha = entry_senha.get()
    confirmar = entry_confirmar.get()

    if not (nome and sobrenome and cpf and senha and confirmar):
        messagebox.showwarning("Erro", "Preencha todos os campos obrigatórios.")
        return

    if senha != confirmar:
        messagebox.showwarning("Erro", "As senhas não coincidem.")
        return

    inserir_cliente(nome, sobrenome, cpf, telefone, senha)
    messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
    listar()

def listar():
    lista.delete(0, tk.END)
    clientes = buscar_clientes()
    for c in clientes:
        lista.insert(tk.END, f"{c[0]} - {c[1]} {c[2]} - CPF: {c[3]}")

def excluir():
    selecionado = lista.curselection()
    if selecionado:
        item = lista.get(selecionado)
        id_cliente = int(item.split(" - ")[0])
        excluir_cliente(id_cliente)
        messagebox.showinfo("Removido", "Cliente excluído com sucesso.")
        listar()

# Interface
janela = tk.Tk()
janela.title("Cadastro de Clientes")

tk.Label(janela, text="Nome").grid(row=0, column=0)
tk.Label(janela, text="Sobrenome").grid(row=1, column=0)
tk.Label(janela, text="CPF").grid(row=2, column=0)
tk.Label(janela, text="Telefone").grid(row=3, column=0)
tk.Label(janela, text="Senha").grid(row=4, column=0)
tk.Label(janela, text="Confirmar Senha").grid(row=5, column=0)

entry_nome = tk.Entry(janela)
entry_sobrenome = tk.Entry(janela)
entry_cpf = tk.Entry(janela)
entry_telefone = tk.Entry(janela)
entry_senha = tk.Entry(janela, show="*")
entry_confirmar = tk.Entry(janela, show="*")

entry_nome.grid(row=0, column=1)
entry_sobrenome.grid(row=1, column=1)
entry_cpf.grid(row=2, column=1)
entry_telefone.grid(row=3, column=1)
entry_senha.grid(row=4, column=1)
entry_confirmar.grid(row=5, column=1)

tk.Button(janela, text="Cadastrar", command=cadastrar).grid(row=6, column=0, columnspan=2, pady=5)
tk.Button(janela, text="Excluir Selecionado", command=excluir).grid(row=7, column=0, columnspan=2, pady=5)

lista = tk.Listbox(janela, width=50)
lista.grid(row=8, column=0, columnspan=2)

listar()

janela.mainloop()
