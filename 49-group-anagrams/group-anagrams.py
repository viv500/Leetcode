class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """


        # slower approach: store sorted string as key and words as values in a list
        # Time: O(n * k log k)
        # Space: O(k) per wordSpace: O(k) per word

        strings = {}
        for word in strs:
            sorted_word = ''.join(sorted(word)) # need to use sorted! sort would modifiy the original
            if sorted_word in strings:
                strings[sorted_word].append(word)
            else:
                strings[sorted_word] = [word]


        # to values
        return [v for v in strings.values()] # each v in strings.values is the array of values

