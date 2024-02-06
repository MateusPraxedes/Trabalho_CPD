from tkinter import *
from tkinter import ttk 
from read_data import le_dados
from pathlib import Path
import pickle

root = Tk()


caminho_projeto = Path()    
path_dados_bin = Path(f"{caminho_projeto.absolute()}\\bin\\steam_data_bin.bin")

class Funcoes():
    def add_jogo(self):
        self.url = self.url_entry.get()
        self.nome = self.nome_entry.get()
        self.categorias = self.categorias_entry.get()
        self.url_imagem = self.img_url_entry.get()
        self.user_reviews = self.user_reviews_entry.get()
        self.data = self.data_entry.get()
        self.desenvolvedora = self.desenvolvedor_entry.get()
        self.distribuidora = self.distribuidora_entry.get()
        self.preco = self.preco_entry.get()

        if not self.url or not self.nome or not self.categorias or not self.url_imagem or not self.user_reviews or not self.data or not self.desenvolvedora or not self.distribuidora or not self.preco:
            print("Por favor, preencha todos os campos.")
            return

        with open(path_dados_bin, 'ab+') as f:
            f.seek(0, 2)  # move the file pointer to the end of the file
            data = {
                'url': self.url,
                'nome': self.nome,
                'categorias': self.categorias,
                'url_imagem': self.url_imagem,
                'user_reviews': self.user_reviews,
                'data': self.data,
                'desenvolvedora': self.desenvolvedora,
                'distribuidora': self.distribuidora,
                'preco': self.preco
            }
            pickle.dump(data, f)
            f.close()
        # Clear the entry fields after adding a game
        self.url_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.categorias_entry.delete(0, END)
        self.img_url_entry.delete(0, END)
        self.user_reviews_entry.delete(0, END)
        self.data_entry.delete(0, END)
        self.desenvolvedor_entry.delete(0, END)
        self.distribuidora_entry.delete(0, END)
        self.preco_entry.delete(0, END)

        # Update the user interface to show the newly added game
        self.dados_jogos()

    def buscar_jogo(self):
        nome_jogo = self.nome_entry3.get()
        dados = le_dados()

        # Substituir os valores nulos pelas strings vazias
        dados.fillna("", inplace=True)

        jogos = dados[dados['name'].str.contains(nome_jogo)]

        if len(jogos) > 0:
            self.table_jogos_buscados.delete(*self.table_jogos_buscados.get_children())
            for index, row in jogos.iterrows():
                self.table_jogos_buscados.insert('', 'end', values=(row['name'], row['url'], row['categories'], row['img_url'], row['user_reviews'], row['date'], row['developer'], row['publisher'], row['price']))
        else:
            self.table_jogos_buscados.delete(*self.table_jogos_buscados.get_children())
            self.table_jogos_buscados.insert('', 'end', values=("Jogo não encontrado.", "", "", "", "", "", "", "", ""))
          
    def atualizar_dados(self):
        self.table_jogos_buscados.delete(*self.table_jogos_buscados.get_children())
        dados = le_dados()
        for index, row in dados.iterrows():
            self.table_jogos_buscados.insert('', 'end', values=(row['name'], row['url'], row['categories'], row['img_url'], row['user_reviews'], row['date'], row['developer'], row['publisher'], row['price']))

class Interface(Funcoes):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_tela()
        self.widgets_tela()
        self.dados_aba_desenvolvedoras()
        self.dados_aba_distribuidoras()
        self.dados_aba_best_games()
        self.dados_aba_precos()
        self.dados_aba_todos()
        root.mainloop()

    def tela(self):
        self.root.title("Steam Games")
        self.root.configure(background="#272C30")
        self.root.geometry("1082x691")
        self.root.resizable(True,True)
        self.root.maxsize(width=1082, height=691)
        self.root.minsize(width=541,height=345)
        
    def frames_tela(self):
        self.frame = Frame(self.root, bd = 4, bg='#efe6e6',highlightbackground= '#efbcbc', highlightthickness="2")
        self.frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
    
    def widgets_tela(self):
        self.abas = ttk.Notebook(self.frame)
        self.aba_adicionar = Frame(self.abas)
        self.aba_deletar = Frame(self.abas)
        self.aba_desenvolvedores = Frame(self.abas)
        self.aba_distribuidoras = Frame(self.abas)
        self.aba_precos = Frame(self.abas)
        self.aba_melhores_jogos = Frame(self.abas)
        self.aba_buscar = Frame(self.abas)
        self.aba_todos = Frame(self.abas)
        self.aba_analitcs = Frame(self.abas)
        
        
        self.aba_adicionar.configure(background="lightgray")
        self.aba_deletar.configure(background="lightgray")
        self.aba_desenvolvedores.configure(background="lightgray")
        self.aba_distribuidoras.configure(background="lightgray")
        self.aba_precos.configure(background="lightgray")
        self.aba_melhores_jogos.configure(background="lightgray")
        self.aba_buscar.configure(background="lightgray")
        self.aba_todos.configure(background="lightgray")
        self.aba_analitcs.configure(background="lightgray")
        
        self.abas.add(self.aba_adicionar, text= " Adicionar Dados")
        self.abas.add(self.aba_deletar, text= " Deletar Dados")
        self.abas.add(self.aba_buscar, text= " Buscar Jogo")
        self.abas.add(self.aba_desenvolvedores, text= " Desenvolvedores")
        self.abas.add(self.aba_distribuidoras, text= " Distribuidoras ")
        self.abas.add(self.aba_precos, text= " Preços")
        self.abas.add(self.aba_melhores_jogos, text= " Melhores Jogos")
        self.abas.add(self.aba_todos, text= " Todos Dados")
        self.abas.add(self.aba_analitcs, text= " Analitcs")
        
        self.abas.place(relx=0, rely=0, relwidth=0.98,relheight=0.98)
        
        # Aba Adicionar dados
        self.lb_url_jogo = Label(self.aba_adicionar, text="URL do jogo:", bg ='#dfe3ee',fg = '#107db2')
        self.lb_url_jogo.place(relx=0.01,rely=0.1)
        
        self.url_entry = Entry(self.aba_adicionar)
        self.url_entry.place(relx=0.15,rely=0.1,relwidth=0.8)
        
        self.lb_nome_jogo = Label(self.aba_adicionar, text="Nome:", bg ='#dfe3ee',fg = '#107db2')
        self.lb_nome_jogo.place(relx=0.01,rely=0.2)
        
        self.nome_entry = Entry(self.aba_adicionar)
        self.nome_entry.place(relx=0.15,rely=0.2,relwidth=0.8)
        
        self.lb_categorias = Label(self.aba_adicionar, text="Categorias:", bg ='#dfe3ee',fg = '#107db2')
        self.lb_categorias.place(relx=0.01,rely=0.3)
        
        self.categorias_entry = Entry(self.aba_adicionar)
        self.categorias_entry.place(relx=0.15,rely=0.3,relwidth=0.8)
        
        self.lb_img_url = Label(self.aba_adicionar, text="URL Imagem:", bg ='#dfe3ee',fg = '#107db2')
        self.lb_img_url.place(relx=0.01,rely=0.4)
        
        self.img_url_entry = Entry(self.aba_adicionar)
        self.img_url_entry.place(relx=0.15,rely=0.4,relwidth=0.8)
        
        self.lb_user_reviews = Label(self.aba_adicionar, text="User Reviews:", bg ='#dfe3ee',fg = '#107db2')
        self.lb_user_reviews.place(relx=0.01,rely=0.5)
        
        self.user_reviews_entry = Entry(self.aba_adicionar)
        self.user_reviews_entry.place(relx=0.15,rely=0.5,relwidth=0.8)
       
        self.lb_data = Label(self.aba_adicionar, text="Data Lançamento", bg ='#dfe3ee',fg = '#107db2')
        self.lb_data.place(relx=0.01,rely=0.6)
        
        self.data_entry = Entry(self.aba_adicionar)
        self.data_entry.place(relx=0.15,rely=0.6,relwidth=0.8)
       
        self.lb_desenvolvedor = Label(self.aba_adicionar, text="Desenvolvedora:", bg ='#dfe3ee',fg = '#107db2')
        self.lb_desenvolvedor.place(relx=0.01,rely=0.7)
        
        self.desenvolvedor_entry = Entry(self.aba_adicionar)
        self.desenvolvedor_entry.place(relx=0.15,rely=0.7,relwidth=0.8)
       
        self.lb_distribuidora = Label(self.aba_adicionar, text="Distribuidora:", bg ='#dfe3ee',fg = '#107db2')
        self.lb_distribuidora.place(relx=0.01,rely=0.8)
        
        self.distribuidora_entry = Entry(self.aba_adicionar)
        self.distribuidora_entry.place(relx=0.15,rely=0.8,relwidth=0.8)
        
        self.lb_preco = Label(self.aba_adicionar, text="Preço:", bg ='#dfe3ee',fg = '#107db2')
        self.lb_preco.place(relx=0.01,rely=0.9)
        
        self.preco_entry = Entry(self.aba_adicionar)
        self.preco_entry.place(relx=0.15,rely=0.9,relwidth=0.8)
        
        self.bt_add = Button(self.aba_adicionar, text="Adicionar",command=self.add_jogo)
        self.bt_add.place(relx=0.01,rely=0.02,relwidth=0.1,relheight=0.05)
        ###################
        
        # Aba Deletar Dados
        self.lb_nome_jogo2 = Label(self.aba_deletar, text="Nome do jogo:", bg ='#dfe3ee',fg = '#107db2')
        self.lb_nome_jogo2.place(relx=0.01,rely=0.2)
        
        self.nome_entry2 = Entry(self.aba_deletar)
        self.nome_entry2.place(relx=0.15,rely=0.2,relwidth=0.8)           
     
        self.bt_apagar = Button(self.aba_deletar, text="Apagar")
        self.bt_apagar.place(relx=0.01,rely=0.02,relwidth=0.1,relheight=0.05)
        ###################
        
        # Aba Buscar Jogo
        self.lb_nome_jogo3 = Label(self.aba_buscar, text="Nome do Jogo:", bg ='#dfe3ee',fg = '#107db2')
        self.lb_nome_jogo3.place(relx=0.01,rely=0.2)
        
        self.nome_entry3 = Entry(self.aba_buscar)
        self.nome_entry3.place(relx=0.15,rely=0.2,relwidth=0.8)           
     
        self.bt_buscar = Button(self.aba_buscar, text="Buscar",command=self.buscar_jogo)
        self.bt_buscar.place(relx=0.01,rely=0.02,relwidth=0.1,relheight=0.05)
        
        self.bt_atualizar = Button(self.aba_buscar, text="Atualizar",command=self.atualizar_dados)
        self.bt_atualizar.place(relx=0.18,rely=0.02,relwidth=0.1,relheight=0.05)
        
            # Adicionar tabela para exibir os jogos buscados
        self.table_jogos_buscados = ttk.Treeview(self.aba_buscar, height=10, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9"))
        self.table_jogos_buscados.column("#0", width=0, stretch=NO)
        self.table_jogos_buscados.heading("#1", text="Nome")
        self.table_jogos_buscados.heading("#2", text="URL")
        self.table_jogos_buscados.heading("#3", text="Categorias")
        self.table_jogos_buscados.heading("#4", text="URL Imagem")
        self.table_jogos_buscados.heading("#5", text="User Reviews")
        self.table_jogos_buscados.heading("#6", text="Data")
        self.table_jogos_buscados.heading("#7", text="Desenvolvedora")
        self.table_jogos_buscados.heading("#8", text="Distribuidora")
        self.table_jogos_buscados.heading("#9", text="Preço")

        self.table_jogos_buscados.column("#1", width=100)
        self.table_jogos_buscados.column("#2", width=100)
        self.table_jogos_buscados.column("#3", width=100)
        self.table_jogos_buscados.column("#4", width=100)
        self.table_jogos_buscados.column("#5", width=100)
        self.table_jogos_buscados.column("#6", width=100)
        self.table_jogos_buscados.column("#7", width=100)
        self.table_jogos_buscados.column("#8", width=100)
        self.table_jogos_buscados.column("#9", width=100)

        self.table_jogos_buscados.place(relx=0.01, rely=0.3, relheight=0.6, relwidth=0.95)

        self.scrollTableJogosBuscados = Scrollbar(self.aba_buscar, orient="vertical")
        self.table_jogos_buscados.configure(yscroll=self.scrollTableJogosBuscados.set)
        self.scrollTableJogosBuscados.place(relx=0.96, rely=0.3, relwidth=0.04, relheight=0.6)
        ###################

     
    def dados_aba_desenvolvedoras(self):
        self.table_desenvolvedoras = ttk.Treeview(self.aba_desenvolvedores,height=3,columns=("col1","col2"))
        self.table_desenvolvedoras.heading("#1", text="Desenvolvedora")
        self.table_desenvolvedoras.heading("#2", text="Quantidade de Jogos")
    
        self.table_desenvolvedoras.column("#0", width=0,stretch=NO)
        self.table_desenvolvedoras.column("#1", width=50)
        self.table_desenvolvedoras.column("#2", width=50)
        
        self.table_desenvolvedoras.place(relx= 0.01, rely = 0.1, relheight=0.85,relwidth=0.95)
        
        self.scrollTableDesenvoledoras = Scrollbar(self.aba_desenvolvedores,orient="vertical")
        self.table_desenvolvedoras.configure(yscroll=self.scrollTableDesenvoledoras.set)
        self.scrollTableDesenvoledoras.place(relx = 0.96, rely =0.1,relwidth=0.04, relheight = 0.985)
        

    def dados_aba_distribuidoras(self):  
        self.table_distribuidoras = ttk.Treeview(self.aba_distribuidoras,height=3,columns=("col1","col2"))
        self.table_distribuidoras.heading("#1", text="Distribuidora")
        self.table_distribuidoras.heading("#2", text="Quantidade de Jogos")

        
        self.table_distribuidoras.column("#0", width=0,stretch=NO)
        self.table_distribuidoras.column("#1", width=50)
        self.table_distribuidoras.column("#2", width=50)
        
        self.table_distribuidoras.place(relx= 0.01, rely = 0.1, relheight=0.85,relwidth=0.95)
        
        self.scrollTableDistribuidoras = Scrollbar(self.aba_distribuidoras,orient="vertical")
        self.table_distribuidoras.configure(yscroll=self.scrollTableDistribuidoras.set)
        self.scrollTableDistribuidoras.place(relx = 0.96, rely =0.1,relwidth=0.04, relheight = 0.985)
       
    def dados_aba_precos(self):  
        self.table_precos = ttk.Treeview(self.aba_precos,height=3,columns=("col1","col2"))
        self.table_precos.heading("#1", text="Jogo")
        self.table_precos.heading("#2", text="Preço")

        self.table_precos.column("#0", width=0,stretch=NO)
        self.table_precos.column("#1", width=50)
        self.table_precos.column("#2", width=50)
        
        self.table_precos.place(relx= 0.01, rely = 0.1, relheight=0.85,relwidth=0.95)
        
        self.scrollTablePrecos = Scrollbar(self.aba_precos,orient="vertical")
        self.table_precos.configure(yscroll=self.scrollTablePrecos.set)
        self.scrollTablePrecos.place(relx = 0.96, rely =0.1,relwidth=0.04, relheight = 0.985)
        
    def dados_aba_best_games(self):  
        self.table_melhores_jogos = ttk.Treeview(self.aba_melhores_jogos,height=3,columns=("col1","col2","col3"))
        self.table_melhores_jogos.heading("#1", text="Jogos")
        self.table_melhores_jogos.heading("#2", text=" Data de Lançamento")
        self.table_melhores_jogos.heading("#3", text="User Reviews")

        self.table_melhores_jogos.column("#0", width=0,stretch=NO)
        self.table_melhores_jogos.column("#1", width=50)
        self.table_melhores_jogos.column("#2", width=50)
        self.table_melhores_jogos.column("#3", width=50)
        
        self.table_melhores_jogos.place(relx= 0.01, rely = 0.1, relheight=0.85,relwidth=0.95)
        
        self.scrollTableMelhoresJogos = Scrollbar(self.aba_melhores_jogos,orient="vertical")
        self.table_melhores_jogos.configure(yscroll=self.scrollTableMelhoresJogos.set)
        self.scrollTableMelhoresJogos.place(relx = 0.96, rely =0.1,relwidth=0.04, relheight = 0.985)
    
    def dados_aba_todos(self):  
        self.table_todos_jogos = ttk.Treeview(self.aba_todos,height=10,columns=("col1","col2","col3","col4","col5","col6","col7","col8","col9"))
        
        self.table_todos_jogos.column("#0", width=0,stretch=NO)
        self.table_todos_jogos.heading("#1", text="URL")
        self.table_todos_jogos.heading("#2", text=" Nome")
        self.table_todos_jogos.heading("#3", text="Categoria")
        self.table_todos_jogos.heading("#4", text="URL Imagem")
        self.table_todos_jogos.heading("#5", text="User Reviews")
        self.table_todos_jogos.heading("#6", text=" Data")
        self.table_todos_jogos.heading("#7", text="Desenvolvedora")
        self.table_todos_jogos.heading("#8", text="Dsitribuidora")
        self.table_todos_jogos.heading("#9", text="Preco")
        
        self.table_todos_jogos.column("#1", width=50)
        self.table_todos_jogos.column("#2", width=50)
        self.table_todos_jogos.column("#3", width=50)
        self.table_todos_jogos.column("#4", width=50)
        self.table_todos_jogos.column("#5", width=50)
        self.table_todos_jogos.column("#6", width=50)
        self.table_todos_jogos.column("#7", width=50)
        self.table_todos_jogos.column("#8", width=50)
        self.table_todos_jogos.column("#9", width=50)
        
        self.table_todos_jogos.place(relx= 0.01, rely = 0.1, relheight=0.85,relwidth=0.95)
        
        self.scrollTableTodos = Scrollbar(self.aba_todos,orient="vertical")
        self.table_todos_jogos.configure(yscroll=self.scrollTableTodos.set)
        self.scrollTableTodos.place(relx = 0.96, rely =0.1,relwidth=0.04, relheight = 0.985)

        self.dados_jogos()
        
    def dados_jogos(self):
        dados = le_dados()
        for index, row in dados.iterrows():
            self.table_todos_jogos.insert('','end', values=(row['url'],row['name'],row['categories'],row['img_url'],row['user_reviews'],row['date'],row['developer'],row['publisher'],row['price']))
            
    