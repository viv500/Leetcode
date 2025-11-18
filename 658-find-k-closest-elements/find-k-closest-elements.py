class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        # 2 pointer approach -> shrink based on side that has closer element to k O(n - k)

        L = 0
        R = len(arr) - 1

        while R - L + 1 > k: # shrink until window size is k
            if abs(arr[R] - x) < abs(arr[L] - x):
                L += 1
            else:
                R -= 1 # this gives priority to smaller element
        return arr[L:R + 1]

        # brute force -> iterate through all O(n) + O(nlogn) = O(nlogn)
        # broken cuz doesnt prioritse smaller element durng ties
        L = []
        for index, element in enumerate(arr):
            L.append([abs( element - x), index])

        L.sort()
        a = sorted([arr[element[1]] for element in L])
        return a[:k]



        
