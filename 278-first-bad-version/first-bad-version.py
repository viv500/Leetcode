# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2

            if isBadVersion(mid):
                #shrinking the possible area of first bad version
                high = mid - 1
            else:

                # getting rid of all the good versions in our search
                low = mid + 1

        return high + 1
            

        