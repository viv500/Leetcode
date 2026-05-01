# trie
class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        d = self.trie

        for char in word:
            if char not in d:
                d[char] = {}
            d = d[char]

        d["!"] = "!" #terminal character

    def search(self, word: str) -> bool:
        d = self.trie
        # need support for wildcard "."

        def dfs(index, node):
            if index == len(word): return "!" in node

            check = word[index]

            if check == ".":
                for child in node.values():
                    if isinstance(child, dict) and dfs(index + 1, child): return True # true if ANY path works            
            else:
                if check in node:
                    return dfs(index + 1, node[check])
            
            return False


        return dfs(0, d)

