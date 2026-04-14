# can be implemented using TrieNode object or uding nested dictionaries
class Trie:

    def __init__(self):
        self.trie = {}
        
    def insert(self, word: str) -> None:
        d = self.trie
        for char in word:
            if char not in d:
                d[char] = {}
            d = d[char]

        # period mapped with period to indicate end of word
        d['.'] = '.'
        

    def search(self, word: str) -> bool:
        d = self.trie
        for char in word:
            if char not in d:
                return False
            d = d[char]
        
        # needs to end in period
        return True if '.' in d else False
        

    def startsWith(self, prefix: str) -> bool:
        d = self.trie
        for char in prefix:
            if char not in d:
                return False
            d = d[char]

        # doesn't need to end in period
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)