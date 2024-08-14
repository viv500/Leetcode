class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] in "aeiouAEIOU" and s[j] in "aeiouAEIOU":
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i += 1
                j -= 1
            elif s[i] in "aeiouAEIOU" and s[j] not in "aeiouAEIOU":
                j -= 1
            elif s[i] not in "aeiouAEIOU" and s[j] in "aeiouAEIOU":
                i += 1
            else:
                i += 1
                j -= 1

        s = ''.join(s)
        return s
            
            

