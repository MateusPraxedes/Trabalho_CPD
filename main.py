from frames.interface import inicializa_interface
from read_data import le_dados
from trie_tree import Trie
    
def main():
    
    jogos_lidos = le_dados()
    print(jogos_lidos)

#Constrói a árvore Trie a partir dos dados contidos na variável jogos_lidos
    t = Trie()
    for key in jogos_lidos:
        t.insert(key)

    window = inicializa_interface(jogos_lidos)
    
    window.mainloop()

if __name__ == '__main__':
    main()
 