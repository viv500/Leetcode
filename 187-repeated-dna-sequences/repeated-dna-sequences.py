class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        memo = set()
        final = []
        start = 0 
        end = 10
        leng = len(s)
        while end <= leng:
            if s[start: end] in memo and s[start: end] not in final:
                final.append(s[start: end])
            else:
                memo.add(s[start: end])
            end += 1
            start += 1
        return final