class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def calculate_sum(n):
            new = 0
            for c in str(n):
                new += int(c) ** 2

            return new


        slow = n
        fast = calculate_sum(n)

        while fast != 1:
            slow = calculate_sum(slow)
            fast = calculate_sum(calculate_sum(fast))

            if slow == fast: return False      

        return True
