import pickle
from trie_tree import save_to_file
from trie_tree import load_from_file

def add_word(trie, word):
    # Adiciona uma nova palavra à trie
    index = len(trie.root.children)
    trie.insert(word, index)
    save_to_file()
    return

def update_word_link(trie, word, new_link):
    # Atualiza o link associado a uma palavra na trie
    exists, index = trie.search(word)
    if exists:
        remove_word(trie, word)
    else:
        print("O dado a ser atualizado não existe!")
        return

    add_word(trie, word)

    save_to_file()
    return

def remove_word(trie, word):
    # Remove uma palavra da trie
    node = trie.root
    parent_nodes = []

    # Encontrar a palavra na trie
    for char in word:
        if char not in node.children:
            return  # A palavra não está na trie
        parent_nodes.append(node)
        node = node.children[char]

    # Remover a palavra a partir do último nó
    node.is_end_of_word = False

    # Verificar se é possível remover os nós intermediários
    while parent_nodes:
        parent_node = parent_nodes.pop()
        char = word[len(parent_nodes)]
        current_node = parent_node.children[char]

        if current_node.is_end_of_word or current_node.children:
            # Se o nó atual ainda é uma palavra ou tem filhos, não podemos removê-lo
            break
        else:
            # Caso contrário, removemos o nó
            del parent_node.children[char]

    save_to_file()
    return

#Implementar na interface
def buscar_e_mostrar_resultados(trie, termo_busca, ordenacao, pagina, registros_por_pagina):
    # Realiza a busca na Trie
    indices_resultado = trie.search(termo_busca)

    # Ordena os resultados conforme especificado
    if ordenacao == 'crescente':
        indices_resultado = sorted(indices_resultado)
    elif ordenacao == 'decrescente':
        indices_resultado = sorted(indices_resultado, reverse=True)

    # Aplica a paginacao
    inicio = (pagina - 1) * registros_por_pagina
    fim = inicio + registros_por_pagina
    resultados_paginados = indices_resultado[inicio:fim]

    # Exibe os resultados paginados
    for indice in resultados_paginados:
        print(f"Registro {indice}: {registros[indice]}")