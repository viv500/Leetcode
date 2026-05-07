from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # shortest sequence: bfs
        # beginWord doesn't need to be in list, but all other (including end) should be in list

        q = deque([(0, beginWord)])
        visited = set()
    

        while q:
            step, word = q.popleft()

            if word == endWord: return step + 1

            for i in range(len(word)):
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + letter + word[i + 1:]
                    if new_word in wordList and new_word not in visited:
                        visited.add(new_word)
                        q.append((step + 1, new_word))

        return 0
    