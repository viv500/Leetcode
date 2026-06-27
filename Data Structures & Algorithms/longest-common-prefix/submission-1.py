class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""

        word1 = strs[0]
        longest = len(word1)


        for word in strs[1:]:
            match = 0
            for i in range(min(len(word1), len(word))):
                if word[i] == word1[i]:
                    match += 1
                else:
                    break
            longest = min(longest, match)

        return word1[:longest]

        
