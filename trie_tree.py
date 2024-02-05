#Função de contrução de uma árvore Trie
import os
import pickle

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.index = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, index):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.index = index

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False, None
            node = node.children[char]
        return node.is_end_of_word, node.index

    def save_to_file(self, file_path):
        with open(file_path, 'wb') as binary_file:
            pickle.dump(self.root, binary_file)

    @classmethod
    def load_from_file(cls, file_path):
        trie = cls()
        with open(file_path, 'rb') as binary_file:
            trie.root = pickle.load(binary_file)
        return trie

def build_trie_from_binary_file(file_path):
    trie = Trie()
    with open(file_path, 'rb') as binary_file:
        index = 0
        while True:
            try:
                data = pickle.load(binary_file)
                if isinstance(data, tuple) and len(data) == 2:
                    word, link = data
                    trie.insert(word, index)
                    index += 1
            except EOFError:
                break
    return trie



