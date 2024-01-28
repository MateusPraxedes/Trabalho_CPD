import tkinter as tk
from action_botoes.action_desenvolvedores import printa as desenvolvedores  
from action_botoes.action_distribuidoras import printa as distribuidoras
from action_botoes.action_best_games import printa as  best_games
from action_botoes.action_precos import printa  as precos

# Cria janela do app
window = tk.Tk()
window.title("Steam Games")
window.geometry("1082x691")

# Define janela as resizable
window.resizable(True, True)

# Adapta o tamanho da sidebar e da main da janela
sidebar_width = int(window.winfo_screenwidth() * 0.15)
main_space_width = window.winfo_screenwidth() - sidebar_width
sidebar_height = window.winfo_screenheight()
main_space_height = window.winfo_screenheight()

# Cria sidebar com os botões
sidebar_frame = tk.Frame(window, width=sidebar_width, height=sidebar_height, bg="#272C30")
sidebar_frame.pack(side="left", fill="both")

# Adiciona título
title_label = tk.Label(sidebar_frame, text="Steam Games", bg="#272C30", fg="white", font=("Helvetica", 16, "bold"))
title_label.place(x=10, y=10)

#Adiciona botões
button_frame = tk.Frame(sidebar_frame, bg="#272C30")
button_frame.place(x=25, y=50)

btn_desenvolvedores = tk.Button(button_frame, text="Desenvolvedores", bg="#333", fg="white", font=("Helvetica", 12), width=15, height=2, relief="flat", bd=0, command=desenvolvedores)
btn_desenvolvedores.grid(row=0, column=0, padx=15, pady=15, columnspan=1, sticky="nsew")

btn_best_games = tk.Button(button_frame, text="Melhores Jogos", bg="#333", fg="white", font=("Helvetica", 12), width=15, height=2, relief="flat", bd=0, command= best_games )
btn_best_games.grid(row=1, column=0, padx=15, pady=15, columnspan=1, sticky="nsew")

btn_distribuidoras = tk.Button(button_frame, text="Distribuidoras", bg="#333", fg="white", font=("Helvetica", 12), width=15, height=2, relief="flat", bd=0, command=distribuidoras)
btn_distribuidoras.grid(row=2, column=0, padx=15, pady=15, columnspan=1, sticky="nsew")

btn_precos = tk.Button(button_frame, text="Preços", bg="#333", fg="white", font=("Helvetica", 12), width=15, height=2, relief="flat", bd=0, command=precos)
btn_precos.grid(row=3, column=0, padx=20, pady=15, columnspan=1, sticky="nsew")

# Cria  a área principal onde ficarão as infos conforme o botao que é clicado na sidebar
data_space = tk.Frame(window, width=main_space_width, height=main_space_height, bg="#4e5860")
data_space.pack(side="right", fill="both")

# Roda em loop a aplicação
window.mainloop()