from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)

        def generate_patterns(word):
            result = []
            for i in range(len(word)):
                result.append(word[:i] + "*" + word[i + 1:])
            return result

        for word in wordList:
            patterns = generate_patterns(word)
            for pattern in patterns:
                graph[pattern].append(word)

        q = deque([beginWord])
        visited = set()
        visited.add(beginWord)

        steps = 0
        while q:
            level_size = len(q)
            for _ in range(level_size):
                word = q.popleft()
                if word == endWord: return steps + 1

                patterns = generate_patterns(word)
                for pattern in patterns:
                    for next_word in graph[pattern]:
                        if next_word not in visited:
                            q.append(next_word)
                            visited.add(next_word)

            steps += 1

        
        return 0

