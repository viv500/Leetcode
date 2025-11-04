class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        low = 0
        high = len(s) - 1

        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1

        return s

        #damn?
        return s.reverse()