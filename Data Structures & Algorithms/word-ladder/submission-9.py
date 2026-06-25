from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        graph = defaultdict(list)
        visited = set()

        def generate_combos(word):
            output = []
            for i in range(len(word)):
                new = word[:i] + "*" + word[i + 1:]
                output.append(new)
            
            return output


        for word in wordList:
            combos = generate_combos(word)
            for combo in combos:
                graph[combo].append(word)

        
        length = 0
        q = deque([beginWord])

        while q:
            length += 1
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord: return length


                for combo in generate_combos(word):
                    for next_word in graph[combo]:
                        if next_word not in visited:
                            q.append(next_word)
                            visited.add(next_word)

        return 0