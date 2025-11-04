class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # avoid insert(), needs extra memory and time. dont add from front, harder to keep track


        # add from back where spaces are empty (0s)

        i = m - 1  # last valid element in nums1
        j = n - 1  # last element in nums2
        k = m + n - 1  # end of nums1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

            # this guarentees we dont overwrite anything we may need


        