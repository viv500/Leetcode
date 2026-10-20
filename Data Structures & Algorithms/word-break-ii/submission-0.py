class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        path = []
        result = []

        def backtrack(start, current):
            if start == len(s):
                result.append(" ".join(path))
                return 

            if current > len(s): return
            
            word = s[start:current]
            if word in wordDict:
                path.append(word)
                backtrack(current, current)
                path.pop()
            
            backtrack(start, current + 1)

        backtrack(0, 0)
        return result

