class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        # if we sort list, it is sufficicent to check common prefix of first and list words

        strs = sorted(strs)
        length = min(len(strs[0]), len(strs[-1]))

        result = ""

        for i in range(length):
            if strs[0][i] == strs[-1][i]:
                result += strs[0][i]
            else:
                # need to break or it will find common character in between, not a prefix
                break

        return result