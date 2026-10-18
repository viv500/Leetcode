class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {} 
            d = d[c]

        d["!"] = word

    def search(self, word: str) -> bool:
        def dfs(d, index):
            if index == len(word): return "!" in d
            
            char = word[index]
            if char == ".":
                for c in d:
                    if dfs(d[c], index + 1):
                        return True
                return False
            elif char in d:
                return dfs(d[char], index + 1)
            else:
                return False

        return dfs(self.trie, 0)


        
