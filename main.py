from frames.interface import inicializa_interface
from read_data import le_dados
from trie_tree import build_trie_from_binary_file
    
def main():
    
    jogos_lidos = le_dados()
    print(jogos_lidos)

#Constrói a árvore Trie a partir dos dados contidos na variável jogos_lidos
    bin_directory = os.path.join(os.path.dirname(__file__), 'bin')
    file_path = os.path.join(bin_directory, 'steam_data_bin.bin')

    if not os.path.exists(file_path):
        print(f"O arquivo binário '{file_path}' não foi encontrado.")
        return

    trie = build_trie_from_binary_file(file_path)

    window = inicializa_interface(jogos_lidos)
    
    window.mainloop()

if __name__ == '__main__':
    main()
 