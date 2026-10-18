from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        steps = 0

        def neis(word):
            result = []
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    result.append(word[:i] + c + word[i + 1:])

            return result

        q = deque([beginWord])
        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord: return steps + 1

                for nei in neis(w):
                    if nei in wordList:
                        wordList.remove(nei)
                        q.append(nei)


            steps += 1

        return 0
