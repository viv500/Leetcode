class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # optimal space: use 1 dictionary and decrement in second round
        # space is O(1) cuz the number of alphabets is fixed. there can only be upto 26 hashmap entries
        # hashmap

        # checks avoids extra space
        if len(s) != len(t):
            return False
            
        chars = {}

        for character in s:
            if character in chars:
                chars[character] += 1
            else:
                chars[character] = 1

        for character in t:
            if character not in chars or chars[character] < 1:
                return False
            else:
                chars[character] -= 1

        return True

        