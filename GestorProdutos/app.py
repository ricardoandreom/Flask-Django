from tkinter import ttk
from tkinter import *
import sqlite3


class Produto:
    db = 'database/produtos.db'

    def db_consulta(self, consulta, parametros=()):
        with sqlite3.connect(self.db) as con:  # Iniciamos uma conexão com a base de dados (alias con)
            cursor = con.cursor() # Criamos um cursor da conexão para poder operar na base de dados
            resultado = cursor.execute(consulta, parametros) # Preparar a consulta SQL (com parâmetros se os há)
            con.commit() # Executar a consulta SQL preparada anteriormente
            return resultado # Restituir o resultado da consulta SQL

    def get_produtos(self):
        # O primeiro, ao iniciar a app, vamos limpar a tabela se tiver dados residuais ou antigos
        registos_tabela = self.tabela.get_children()  # Obter todos os dados da tabela
        for linha in registos_tabela:
            self.tabela.delete(linha)

        # Consulta SQL
        query = 'SELECT * FROM produto ORDER BY nome DESC'
        registos_db = self.db_consulta(query) # Faz-se a chamada ao método db_consultas
        # Escrever os dados no ecrã
        for linha in registos_db:
            print(linha) # print para verificar por consola os dados
            self.tabela.insert('', 0, text = linha[1], values = linha[2])

    def validacao_nome(self):
        nome_introduzido_por_utilizador = self.nome.get()
        return len(nome_introduzido_por_utilizador) != 0

    def validacao_preco(self):
        preco_introduzido_por_utilizador = self.preco.get()
        return len(preco_introduzido_por_utilizador) != 0

    def add_produto(self):
        if self.validacao_nome() and self.validacao_preco():
            query = 'INSERT INTO produto VALUES(NULL, ?, ?)'  # Consulta SQL (sem os dados)
            parametros = (self.nome.get(), self.preco.get()) # Parâmetros da consulta SQL
            self.db_consulta(query, parametros)
            print("Dados guardados")
            self.mensagem['text'] = 'Produto {} adicionado com êxito'.format(self.nome.get()) # Label localizada entre o botão e a tabela
            self.nome.delete(0,END)  # Apagar o campo nome do formulário
            self.preco.delete(0, END) # Apagar o campo preço do formulário

            # Para debug
            # print(self.nome.get())
            # print(self.preço.get())
        elif self.validacao_nome() and self.validacao_preco()==False:
            self.mensagem['text'] = 'O preço é obrigatório'
        elif self.validacao_nome()==False and self.validacao_preco():
            self.mensagem['text'] = 'O nome é obrigatório'
        else:
            self.mensagem['text'] = 'O nome e o preço são obrigatórios'

        self.get_produtos() # Quando se finalizar a inserção de dados voltamos a invocar este método para atualizar o conteúdo e ver as alterações

    def del_produto(self):
        # Debug
        # print(self.tabela.item(self.tabela.selection()))
        # print(self.tabela.item(self.tabela.selection())['text'])
        # print(self.tabela.item(self.tabela.selection())['values'])
        # print(self.tabela.item(self.tabela.selection())['values'][0])

        self.mensagem['text'] = ''  # Mensagem inicialmente vazio
        # Comprovação de que se selecione um produto para poder eliminá-lo
        try:
            self.tabela.item(self.tabela.selection())['text'][0]
        except IndexError as e:
            self.mensagem['text'] = 'Por favor, selecione um produto'
            return

        self.mensagem['text'] = ''
        nome = self.tabela.item(self.tabela.selection())['text']
        query = 'DELETE FROM produto WHERE nome = ?' # Consulta SQL
        self.db_consulta(query, (nome,)) # Executar a consulta
        self.mensagem['text'] = 'Produto {} eliminado com êxito'.format(nome)
        self.get_produtos() # Atualizar a tabela de produtos

    def edit_produto(self):
        self.mensagem['text'] = ''  # Mensagem inicialmente vazia
        try:
            self.tabela.item(self.tabela.selection())['text'][0]
        except IndexError as e:
            self.mensagem['text'] = 'Por favor, selecione um produto'
            return

        nome = self.tabela.item(self.tabela.selection())['text']
        old_preco = self.tabela.item(self.tabela.selection())['values'][0] # O preço encontra-se dentro de uma lista
        self.janela_editar = Toplevel() # Criar uma janela à frente da principal
        self.janela_editar.title = "Editar Produto" # Titulo da janela
        self.janela_editar.resizable(1, 1) # Ativar a redimensão da janela. Para desativá-la: (0,0)
        self.janela_editar.wm_iconbitmap('recursos/icon.ico') # Ícone da janela

        titulo = Label(self.janela_editar, text='Edição de Produtos', font=('Calibri', 50, 'bold'))
        titulo.grid(column=0, row=0)
        # Criação do recipiente Frame da janela de Editar Produto
        frame_ep = LabelFrame(self.janela_editar, text="Editar o seguinte Produto", font=('Calibri', 16, 'bold')) # frame_ep: Frame Editar Produto
        frame_ep.grid(row=1, column=0, columnspan=20, pady=20)

        # Label Nome antigo
        self.etiqueta_nome_antigo = Label(frame_ep, text="Nome antigo: ", font=('Calibri', 13))
        # Etiqueta de texto localizada no frame
        self.etiqueta_nome_antigo.grid(row=2, column=0)
        # Posicionamento através de grid # Entry Nome antigo (texto que não se poderá modificar)
        self.input_nome_antigo = Entry(frame_ep, textvariable=StringVar(self.janela_editar, value=nome),
                                       state='readonly', font=('Calibri', 13))
        self.input_nome_antigo.grid(row=2, column=1)
        # Label Nome novo
        self.etiqueta_nome_novo = Label(frame_ep, text="Nome novo: ", font=('Calibri', 13))
        self.etiqueta_nome_novo.grid(row=3, column=0)
        # Entry Nome novo (texto que se poderá modificar)
        self.input_nome_novo = Entry(frame_ep, font=('Calibri', 13))
        self.input_nome_novo.grid(row=3, column=1)
        self.input_nome_novo.focus()  # Para que a seta do rato vá a esta Entry ao início
        # Label Preço antigo
        self.etiqueta_preco_antigo = Label(frame_ep, text="Preço antigo: ", font=('Calibri', 13))
        # Etiqueta de texto localizada no frame
        self.etiqueta_preco_antigo.grid(row=4, column=0)  # Posicionamento através de grid
        # Entry Preço antigo (texto que não se poderá modificar)
        self.input_preco_antigo = Entry(frame_ep, textvariable=StringVar(self.janela_editar, value=old_preco),
                                        state='readonly', font=('Calibri', 13))
        self.input_preco_antigo.grid(row=4, column=1)
        # Label Preço novo
        self.etiqueta_preco_novo = Label(frame_ep, text="Preço novo: ", font=('Calibri', 13))
        self.etiqueta_preco_novo.grid(row=5, column=0)
        # Entry Preço novo (texto que se poderá modificar)
        self.input_preco_novo = Entry(frame_ep, font=('Calibri', 13))
        self.input_preco_novo.grid(row=5, column=1)

        # Botão Atualizar Produto
        s = ttk.Style()
        s.configure('my.TButton', font=('Calibri', 14, 'bold'))
        self.botao_atualizar = ttk.Button(frame_ep, text="Atualizar Produto", style='my.TButton',
                                          command=lambda: self.atualizar_produtos(self.input_nome_novo.get(),
                                                                                  self.input_nome_antigo.get(),
                                                                                  self.input_preco_novo.get(),
                                                                                  self.input_preco_antigo.get()))
        self.botao_atualizar.grid(row=6, columnspan=2, sticky=W + E)

    def atualizar_produtos(self, novo_nome, antigo_nome, novo_preco, antigo_preco):
        produto_modificado = False

        query = 'UPDATE produto SET nome = ?, preco = ? WHERE nome = ? AND preco = ?'
        if novo_nome != '' and novo_preco != '':
            # Se o utilizador escreve novo nome e novo preço, mudam-se ambos
            parametros = (novo_nome, novo_preco, antigo_nome, antigo_preco)
            produto_modificado = True
        elif novo_nome != '' and novo_preco == '': # Se o utilizador deixa vazio o novo preço, mantém-se o preço anterior
            parametros = (novo_nome, antigo_preco, antigo_nome, antigo_preco)
            produto_modificado = True
        elif novo_nome == '' and novo_preco != '': # Se o utilizador deixa vazio o novo nome, mantém-se o nome anterior
            parametros = (antigo_nome, novo_preco, antigo_nome, antigo_preco)
            produto_modificado = True

        if produto_modificado:
            self.db_consulta(query, parametros)
            self.mensagem['text'] = 'Produto {} atualizado com êxito'.format(antigo_nome)
            self.janela_editar.destroy()
            self.get_produtos()
        else:
            self.mensagem['text'] = 'Nenhuma modificação foi feita'

    def __init__(self, window):
        self.janela = window
        self.janela.title("Gestão de Produtos")
        self.janela.geometry('850x600')
        self.janela.resizable(0, 0)

        # Adicionar um título
        titulo = Label(self.janela, text='Gestão de Produtos', font=('Calibri', 24, 'bold'))
        titulo.grid(row=0, column=0, columnspan=2)

        # Frame para Registar um novo Produto
        frame = LabelFrame(self.janela, text="Registar um novo Produto", font=('Calibri', 16, 'bold'))
        frame.grid(row=1, column=0, columnspan=2, pady=20)

        # Nome
        self.etiqueta_nome = Label(frame, text="Nome: ", font=('Calibri', 13))
        self.etiqueta_nome.grid(row=1, column=0)
        self.nome = Entry(frame, font=('Calibri', 13))
        self.nome.grid(row=1, column=1)

        # Preço
        self.etiqueta_preco = Label(frame, text="Preço: ", font=('Calibri', 13))
        self.etiqueta_preco.grid(row=2, column=0)
        self.preco = Entry(frame, font=('Calibri', 13))
        self.preco.grid(row=2, column=1)

        # Botão Adicionar Produto
        s = ttk.Style()
        s.configure('my.TButton', font=('Calibri', 14, 'bold'))
        self.botao_adicionar = ttk.Button(frame, text="Guardar Produto", command=self.add_produto, style='my.TButton')
        self.botao_adicionar.grid(row=3, columnspan=2, sticky=W + E)

        # Mensagem de saída para o utilizador
        self.mensagem = Label(text='', fg='red')
        self.mensagem.grid(row=3, column=0, columnspan=2, sticky=W + E)

        # Tabela de produtos
        self.tabela = ttk.Treeview(height=10, columns=2)
        self.tabela.grid(row=4, column=0, columnspan=2)
        self.tabela.heading('#0', text='Nome', anchor=CENTER)
        self.tabela.heading('#1', text='Preço', anchor=CENTER)

        # Botões de Eliminar e Editar
        botao_eliminar = ttk.Button(text='ELIMINAR', command=self.del_produto, style='my.TButton')
        botao_eliminar.grid(row=5, column=0, sticky=W + E)
        botao_editar = ttk.Button(text='EDITAR', command=self.edit_produto, style='my.TButton')
        botao_editar.grid(row=5, column=1, sticky=W + E)

        # Preencher a tabela com produtos
        self.get_produtos()


if __name__ == "__main__":
    root = Tk()
    app = Produto(root)
    root.mainloop()
