class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        trie = self.trie

        for c in word:
            if c not in trie:
                trie[c] = {}

            trie = trie[c]

        trie["!"] = "!"


    def search(self, word: str) -> bool:
        trie = self.trie

        def dfs(trie, index):
            if index == len(word): return "!" in trie

            char = word[index]
            if char == ".":
                for c in trie:
                    if c != "!" and dfs(trie[c], index + 1):
                        return True
                return False
            elif char not in trie:
                return False
            else:
                return dfs(trie[char], index + 1)

        return dfs(trie, 0)

        
