class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        d = self.trie

        for char in word:
            if char not in d:
                d[char] = {}
            d = d[char]

        d['!'] = "!"

    def search(self, word: str) -> bool:

        def dfs(index, node):
            if index == len(word):          # consumed all chars
                return "!" in node          # valid only if word ends here
            
            check = word[index]
            if check == ".":
                for child in node.values():
                    if isinstance(child, dict) and dfs(index + 1, child): return True
            else:
                if check in node:
                    return dfs(index + 1, node[check])
            
            return False
        
        return dfs(0, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)