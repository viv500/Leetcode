from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for word in strs:
            freq = [0] * 26

            for char in word:
                freq[ord(char) - ord('a')] += 1

            # lists can't be dictionary keys
            freq = tuple(freq)
            output[freq].append(word)

        return [words for words in output.values()]