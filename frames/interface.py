from tkinter import *
from tkinter import ttk 

root = Tk()
class Interface():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_tela()
        self.widgets_tela()
        self.dados_aba_desenvolvedoras()
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
        
        self.aba_adicionar.configure(background="lightgray")
        self.aba_deletar.configure(background="lightgray")
        self.aba_desenvolvedores.configure(background="lightgray")
        self.aba_distribuidoras.configure(background="lightgray")
        self.aba_precos.configure(background="lightgray")
        self.aba_melhores_jogos.configure(background="lightgray")
        self.aba_buscar.configure(background="lightgray")
        
        self.abas.add(self.aba_adicionar, text= " Adicionar Dados")
        self.abas.add(self.aba_deletar, text= " Deletar Dados")
        self.abas.add(self.aba_buscar, text= " Buscar Jogo")
        self.abas.add(self.aba_desenvolvedores, text= " Desenvolvedores")
        self.abas.add(self.aba_distribuidoras, text= " Distribuidoras ")
        self.abas.add(self.aba_precos, text= " Preços")
        self.abas.add(self.aba_melhores_jogos, text= " Melhores Jogos")
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
       
        self.lb_distribuidora = Label(self.aba_adicionar, text="Distribuidaora:", bg ='#dfe3ee',fg = '#107db2')
        self.lb_distribuidora.place(relx=0.01,rely=0.8)
        
        self.distribuidora_entry = Entry(self.aba_adicionar)
        self.distribuidora_entry.place(relx=0.15,rely=0.8,relwidth=0.8)
        
        self.lb_preco = Label(self.aba_adicionar, text="Preço:", bg ='#dfe3ee',fg = '#107db2')
        self.lb_preco.place(relx=0.01,rely=0.9)
        
        self.preco_entry = Entry(self.aba_adicionar)
        self.preco_entry.place(relx=0.15,rely=0.9,relwidth=0.8)
        
        self.bt_add = Button(self.aba_adicionar, text="Adicionar")
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
     
        self.bt_buscar = Button(self.aba_buscar, text="Buscar")
        self.bt_buscar.place(relx=0.01,rely=0.02,relwidth=0.1,relheight=0.05)
        ###################

    def dados_aba_adicionar(self):  
            self.

     
     
    def dados_aba_desenvolvedoras(self):
        self.table_desenvolvedoras = ttk.Treeview(self.aba_desenvolvedores,height=3,columns=("col1","col2",))
        self.table_desenvolvedoras.heading("#1", text="Desenvolvedora")
        self.table_desenvolvedoras.heading("#2", text="Quantidade de Jogos")

        self.table_desenvolvedoras.column("#1", width=50)
        self.table_desenvolvedoras.column("#2", width=50)
        
        self.table_desenvolvedoras.place(relx= 0.01, rely = 0.1, relheight=0.85,relwidth=0.95)
        
        self.scrollTableDesenvoledoras = Scrollbar(self.aba_desenvolvedores,orient="vertical")
        self.table_desenvolvedoras.configure(yscroll=self.scrollTableDesenvoledoras.set)
        self.scrollTableDesenvoledoras.place(relx = 0.96, rely =0.1,relwidth=0.04, relheight = 0.985)
       
