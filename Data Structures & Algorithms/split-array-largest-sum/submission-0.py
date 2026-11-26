class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        lo, hi = max(nums), sum(nums)
        best = hi

        def feasible(max_sum):
            m = k
            total = 0

            for num in nums:
                total += num
                if total > max_sum:
                    total = num
                    m -= 1

            return m > 0

        while lo <= hi:
            mid = (lo + hi) // 2

            if feasible(mid):
                best = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return best



