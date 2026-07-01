
from collections import defaultdict 
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)
        state = {}
        output = []

        for i in range(1, len(words)):
            word1, word2 = words[i - 1], words[i]

            j = 0
            max_j = min(len(word1), len(word2))
            # stop at the first mismatch
            while j < max_j and word1[j] == word2[j]:
                j += 1

                

            # case where prefix comes after 
            if j == len(word2) and j != len(word1): return ""

            # create graph edge
            if j < len(word1) and j < len(word2):
                graph[word1[j]].append(word2[j])

        
        print(graph)
        for word in words:
            for char in word:
                state[char] = 0

        def dfs(char):
            if state[char] == 2: return True
            if state[char] == 1: return False

            state[char] = 1
            for nei in graph[char]:
                if not dfs(nei): return False
            
            state[char] = 2
            output.append(char)
            return True

        for char in state:
            if not dfs(char): return ""

        return "".join(output[::-1])
    




        