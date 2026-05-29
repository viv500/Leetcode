from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        visited = set()
        wordList = set(wordList)
        pattern_map = defaultdict(list)

        def getPatterns(word):
            patterns = []
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                patterns.append(pattern)
            return patterns

        for word in wordList:
            for pattern in getPatterns(word):
                pattern_map[pattern].append(word)

        print(pattern_map)

        q = deque([beginWord])
        step = 1

        while q:
            level_size = len(q)

            for _ in range(level_size):
                word = q.popleft()
                if word == endWord: return step

                for pattern in getPatterns(word):
                    for word in pattern_map[pattern]:
                        if word not in visited:
                            visited.add(word)
                            q.append(word)

            step += 1

        return 0

