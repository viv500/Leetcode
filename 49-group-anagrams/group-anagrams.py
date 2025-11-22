from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            word = ''.join(sorted(s))
            hashmap[word].append(s)
        
        return [v for v in hashmap.values()]