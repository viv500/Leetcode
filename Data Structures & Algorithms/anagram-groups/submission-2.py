from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord('a') - ord(c)] += 1

            anagrams[tuple(freq)].append(s)

        
        return list(anagrams.values())

            

        