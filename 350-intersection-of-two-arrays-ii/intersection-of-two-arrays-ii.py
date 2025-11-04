class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        d1 = {}
        d2 = {}

        for number in nums1:
            if number in d1:
                d1[number] += 1
            else:
                d1[number] = 1


        for number in nums2:
            if number in d2:
                d2[number] += 1
            else:
                d2[number] = 1


        L = []
        for item in d1:
            if item in d2:
                L.extend([item] * min(d1[item], d2[item]))


        return L