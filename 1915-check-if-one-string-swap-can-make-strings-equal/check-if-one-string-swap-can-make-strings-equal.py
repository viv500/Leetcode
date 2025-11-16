class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # O(n) time and O(1) space cuz we return false immeditaely if there are more than 2 mismatches
        # track how many mismatched character we have: more than 2-> false

        if s1 == s2: return True

        mismatch = []

        for index in range(len(s1)): # s1 and s2 are known to have equal length
            if s1[index] != s2[index]:
                mismatch.append(index)
                if len(mismatch) > 2: return False

        if len(mismatch) != 2: return False # could be 1, also doesn't work . could cause index error at the end

        # cant swap like this how youd do in a list: s2[mismatch[0]], s2[mismatch[1]] = s2[mismatch[1]], s2[mismatch[0]]
        # cannot change a specific character in a string like s2[mismatch[0]] = "a"
        
        i, j = mismatch
        return s1[i] == s2[j] and s1[j] == s2[i]
        # compare the characters not the strings! compare both ways

