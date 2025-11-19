class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        L = s.split()
  
        mapping_1 = {}
        mapping_2 = {}

        if len(L) != len(pattern): return False # cant be a mapping


        # need to check btth ways to ensure bijection
        for i in range(len(pattern)):
            if pattern[i] not in mapping_1:
                mapping_1[pattern[i]] = L[i]
            else:
                if mapping_1[pattern[i]] != L[i]:
                    return False

            if L[i] not in mapping_2:
                mapping_2[L[i]] = pattern[i]
            else:
                if mapping_2[L[i]] != pattern[i]:
                    return False

        return True
            
