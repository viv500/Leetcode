class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        longest = [1] * len(words)
        words.sort(key = lambda w: len(w))

        def is_pred(a, b):
            for i in range(len(b)):
                new = b[:i] + b[i + 1:]
                if new == a: return True

            return False

        for i in range(len(words)):
            for j in range(i):
                prev, nxt = words[j], words[i]
                if abs(len(prev) - len(nxt)) != 1: continue
                if is_pred(prev, nxt):
                    longest[i] = max(longest[i], longest[j] + 1)

        return max(longest)
                