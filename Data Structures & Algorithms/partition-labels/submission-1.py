from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # time and space: O(n)
        last_char_index = defaultdict(int) 
        # maps every character to the index of its last occurance in the string

        for index, char in enumerate(s):
            last_char_index[char] = max(last_char_index[char], index)

        index = 0
        output = []

        while index < len(s):
            max_end = last_char_index[s[index]]

            size = 1
            while index < max_end:
                max_end = max(last_char_index[s[index]], max_end)
                index += 1
                size += 1
            
            output.append(size)
            index += 1

        return output

