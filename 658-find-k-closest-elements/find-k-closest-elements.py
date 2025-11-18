class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        # binary search approach: O(log(n - k) + k)
        # binary searching on starting positions for the range
        # We don't need abs because we're not measuring distances, we're checking which side of the window x is leaning towards:

        L = 0
        R = len(arr) - k # left most staring position for window

        while L < R:
            mid = (L + R )// 2
            if x - arr[mid] > arr[mid + k] - x:
                L = mid + 1
            else:
                R = mid

        return arr[L:L+k]


        # 2 pointer sliding window approach -> shrink based on side that has closer element to k O(n - k)

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



        
