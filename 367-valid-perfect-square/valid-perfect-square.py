class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        if num < 0:
            return False
        if num == 1:
            return True

        start = 0
        end = int(num / 2) + 1

        while start <= end:
            mid = int((start + end) //2)

            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                end = mid - 1
            else:
                start = mid + 1
            

        return False