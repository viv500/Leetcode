class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # brute force: merging already sorted array and returning the median O(m + n)

        # binary search on A. for every mid in A, calculate items in the left partition in A
        # based on this and the total number of elements, we can calculate the mid in B

        # correct partition critera. if A[mid] <= B[mid + 1] and B[mid] <= A[mid + 1]
        # if this is true AND we have the right amount of numbers in each partition , if
        #  1. total number of elements was odd, return min(A[mid + 1], B[mid + 1])
        #  2. total number of elements was even, find average of MAX of left partition and MIN of right partition

        # ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        left, right = 0, m

        while True:
            i = (left + right) // 2  # partition in nums1
            j = half - i             # partition in nums2

            # handle edges with -inf and inf
            Aleft = nums1[i - 1] if i > 0 else float('-inf')
            Aright = nums1[i] if i < m else float('inf')
            Bleft = nums2[j - 1] if j > 0 else float('-inf')
            Bright = nums2[j] if j < n else float('inf')

            # check if correct partition
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1

        
    
