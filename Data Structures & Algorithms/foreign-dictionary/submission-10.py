# note: 

from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}

        # need every char
        for word in words:
            for c in word:
                graph[c] = []

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            index = 0
            while index < len(w1) and index < len(w2):
                if w1[index] != w2[index]:
                    graph[w2[index]].append(w1[index])
                    break
                index += 1

            # checking if prefix appears later
            if index == len(w2) and len(w1) > len(w2): return ""
        
        result = []
        visited = set()
        visiting = set()

        def dfs(char):
            if char in visiting: return False
            if char in visited: return True

            visiting.add(char)
            for nei in graph[char]:
                if not dfs(nei): return False

            visiting.remove(char)
            visited.add(char)

            result.append(char)
            return True


        for c in graph:
            if not dfs(c): return ""

        return "".join(result)

        

        