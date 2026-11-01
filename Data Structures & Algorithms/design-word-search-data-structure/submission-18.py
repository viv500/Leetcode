class WordDictionary:

    def __init__(self):
        self.trie = {}
        
    def addWord(self, word: str) -> None:
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            
            t = t[w]
        
        t["!"] = word
        

    def search(self, word: str) -> bool:
        def dfs(i, t):
            if i == len(word): return "!" in t

            c = word[i]
            if c == ".":
                for char in t:
                    if dfs(i + 1, t[char]): return True
                return False
            
            if c in t:
                return dfs(i + 1, t[c])
            else:
                return False

        return dfs(0, self.trie)
        
