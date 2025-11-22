from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for char in s:
                freq[ord(char) - ord('a')] += 1

            freq = tuple(freq)
            hashmap[freq].append(s)

        return [v for v in hashmap.values()]