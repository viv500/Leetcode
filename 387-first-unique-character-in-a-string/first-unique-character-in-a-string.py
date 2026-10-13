class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(list)

        for i, c in enumerate(s):
            count[c].append(i)

        for c in count:
            if len(count[c]) == 1: return count[c][0]
        
        return -1
        