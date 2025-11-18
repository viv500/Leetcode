class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        # edge case
        if len(s) < len(p):
            return []

        # hashmap for anagrams and sliding window to check intervals
        freq = [0] * 26
        for char in p:
            index = ord(char) - ord('a')
            freq[index] += 1

        output = []
        window_size = len(p)

        # initializing hashmap for each window
        freq_inner = [0] * 26
        for char in s[:window_size]: # upper bound exclusive even for slicing
            index = ord(char) - ord('a')
            freq_inner[index] += 1

        p1 = 0
        p2 = window_size # p2 is ahead but its what we wanna "add" for the next round

        while p2 < len(s):
            if freq_inner == freq:
                output.append(p1)

            freq_inner[ord(s[p1]) - ord('a')] -= 1
            freq_inner[ord(s[p2]) - ord('a')] += 1

            p1 += 1 # careful about the order of the frequency table updates and this, you need to remove and add thr correct element
            p2 += 1

        # Check the last window
        if freq_inner == freq:
            output.append(p1)

        return output
