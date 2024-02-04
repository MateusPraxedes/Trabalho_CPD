#Função de contrução de uma árvore Trie para injeção dos dados do arquivo .bin gerado a partir do arquivo .csv em read_data.py

class TrieNode:
    def __init__(self):
        self.children = [None] * 256  # 256 possible characters for binary data
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
        return ch

    def insert(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

        pCrawl.isEndOfWord = True

    def search(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl.isEndOfWord


def read_binary_file(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    return data


