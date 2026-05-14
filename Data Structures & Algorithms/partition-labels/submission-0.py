from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_char_index = defaultdict(int) # maps every character to the index of its last occurance in the string

        for index, char in enumerate(s):
            last_char_index[char] = max(last_char_index[char], index)

        print(last_char_index)

        left = right = 0
        visited = set()
        output = []

        while right < len(s):
            max_end = last_char_index[s[right]]

            size = 1
            while right < max_end and right < len(s):
                max_end = max(last_char_index[s[right]], max_end)
                right += 1
                size += 1
            
            output.append(size)
            right += 1

        return output

