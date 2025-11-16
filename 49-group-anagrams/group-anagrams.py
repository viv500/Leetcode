class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """


        # better approach
        # O(n * k)
        # frequency tuple for characters
    

        strings = {}
        for word in strs:
            freq = [0] * 26
            total = 0
            for char in word:
                index = ord(char) - ord('a') # this maps a -> 0 b -> 1 etc
                freq[index] += 1
            freq = tuple(freq) # CANT USE LIST OR SET HERE: unhashable types
            if freq in strings:
                strings[freq].append(word)
            else:
                strings[freq] = [word]


        # to values
        return [v for v in strings.values()] # each v in strings.values is the array of values

        # summing up unicode values can lead to unequal strings being treated as equals
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

