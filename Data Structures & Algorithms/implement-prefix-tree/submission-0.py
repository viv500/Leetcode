class PrefixTree:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        d = self.trie
        for char in word:
            if char not in d:
                d[char] = {}
            d = d[char]

        d[''] = ''


    def search(self, word: str) -> bool:
        d = self.trie

        for char in word:
            if char not in d:
                return False
            d = d[char]

        return '' in d        

    def startsWith(self, prefix: str) -> bool:
        d = self.trie

        for char in prefix:
            if char not in d:
                return False
            d = d[char]

        return True
        
        