class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        # Q) longest "same character" substring where you can change any k characters
        # sliding window with frequency array. max(frequency array) = the count of the "same character" we want
        # we dont care what the character is, just that it is what we want to flip other characters into
        # logic to find invalid window: if size of current window - max(freq array) > k 
        # i.e. we need to flip more character than we have flips available (k)

        freq = [0] * 26
        L = 0
        longest = 0

        for R in range(len(s)):
            freq[ord(s[R]) - ord('A')] += 1 # check if window is valid after expanding
    
            while((R - L + 1) - max(freq) > k):
                freq[ord(s[L]) - ord('A')] -= 1 # its A here not a
                L += 1

            longest = max(longest, R - L + 1)

        return longest
            