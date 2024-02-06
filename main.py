from frames.interface import Interface
from read_data import le_dados
from trie_tree import Trie
import os

def main():
    
    dados = le_dados()
    
    print(dados.info())

#Constrói a árvore Trie a partir dos dados contidos na variável jogos_lidos
    bin_directory = os.path.join(os.path.dirname(__file__), 'bin')
    file_path = os.path.join(bin_directory, 'steam_data_bin.bin')
    trie_file_path = os.path.join(bin_directory, 'trie_data.bin')

    if os.path.exists(trie_file_path):
        trie = Trie.load_from_file(trie_file_path)
    else:
        trie = Trie.build_trie_from_binary_file(file_path)

    window = Interface()
    window.mainloop()
    
if __name__ == '__main__':
    main()
 