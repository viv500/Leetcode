class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        # idea -> pick the character that has most occurances and try flipping others
        # condition for success -> if number of character that are not our majoirt character is <= k, this is possible!

        # initialize frequency table
        freq = [0] * 26

        L = R = 0
        longest = -1

        while R < len(s):

            freq[ord(s[R]) - ord('A')] += 1
            
            # condition for moving left window
            while((R - L + 1) - max(freq) > k):
                freq[ord(s[L]) - ord('A')] -= 1
                L += 1

            longest = max(longest, R - L + 1)
            R += 1

        return longest
