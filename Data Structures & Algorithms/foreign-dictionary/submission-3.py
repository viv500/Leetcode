from collections import defaultdict
unvisited = 0
visiting = 1
visited = 2
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # TOPOLOGICAL SORTING
        # invalid order: cycle in graph
        # valid ambiguous order: DAG but multiple components -> many possible solutions
        #   ex. a->b->c  d->e->f could be "abcdef" or "defabc" or "adbecf" and so on
        # valid unambiguous order: DAG with single component

        # note: need a node collection step thats separate from edge creation
        # this is cuz not every node had edges, and our edge creation loop terminates at first mismatch
        # problem: some nodes may be ignored cuz of this

        # note: need to separately enforce the prefix rule, since topo sort doesn't find that
        # ex if abc appears before ab in the order

        # 1. finding all nodes
        letters = set()
        for word in words:
            for character in word:
                letters.add(character)

        # 2. forming the graph
        graph = defaultdict(list)
        if len(words) == 1: return words[0]

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            min_length = min(len(word1), len(word2))

            # prefix rule
            if word1[:min_length] == word2 and len(word1) > len(word2): return ""

            for index in range(min_length):
                if word1[index] != word2[index]:

                    # create edge
                    graph[word2[index]].append(word1[index])
                    break

        print(graph)


        # 3. topological sort via dfs

        state = defaultdict(int)
        order = ""

        def dfs(letter):
            nonlocal order
            if state[letter] == visiting: return False
            if state[letter] == visited: return True

            state[letter] = visiting

            for nei in graph[letter]:
                if not dfs(nei): return False

            state[letter] = visited
            order += letter
            return True


        for letter in letters:
            if not dfs(letter): return ""

        return order

            