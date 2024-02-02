from frames.interface import inicializa_interface
from read_data import le_dados

    
def main():
    
    jogos_lidos = le_dados()
    print(jogos_lidos)
    window = inicializa_interface(jogos_lidos)
    
    window.mainloop()

if __name__ == '__main__':
    main()
 