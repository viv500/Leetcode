class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # CANNOT BE SOLVED WITH SLIDING WINDOW 
        # negative numbers allowed!
        # simliar to 2Sum
        # brute force -> O(n^2) nested for loop with additions

        # this is O(n)
        # running prefix sums!


        # if prefix_sum[j] - prefix_sum[i] = k, then subarray [i + 1, j] adds up to k

        count = 0
        cur_sum = 0
        seen = {0 : 1} # This handles the case where a prefix sum itself equals k. For example:

        for num in nums:
            cur_sum += num

            if cur_sum - k in seen:
                count += seen[cur_sum - k] # there could be more than 2 subarray that adds to cur_sum - k
            seen[cur_sum] = seen.get(cur_sum, 0) + 1 # safe way to access dictionary. if cur_sum not found, return 0

        return count

      