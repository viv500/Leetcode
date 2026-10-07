from collections import defaultdict
class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        longest = [1] * len(words)
        words.sort(key = lambda w: len(w))
        longest_chain = {word: 1 for word in words}

        def generate_preds(word):
            result = []
            for i in range(len(word)):
                result.append(word[:i] + word[i + 1:])

            return result

        for word in words:
            preds = generate_preds(word)

            for pred in preds:
                if pred in longest_chain:
                    longest_chain[word] = max(longest_chain[word], 1 + longest_chain[pred])

        return max(longest_chain.values())