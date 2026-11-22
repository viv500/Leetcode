class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie
        for c in word:
            if c not in trie:
                trie[c] = {}
            
            trie = trie[c]

        trie["!"] = word


    def search(self, word: str) -> bool:
        trie = self.trie

        for c in word:
            if c not in trie: return False
            trie = trie[c]

        return "!" in trie
        

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie

        for c in prefix:
            if c not in trie: return False
            trie = trie[c]

        return True
        
        