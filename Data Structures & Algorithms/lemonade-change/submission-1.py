class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # if 5, keep 5, if 10 check 5 change keep 5. if 20. keep 15 but check for both 10 + 5 change and 5 + 5 + 5 change
        change = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            if bill == 5:
                change[5] += 1
            elif bill == 10:
                change[10] += 1
                change[5] -= 1
            else:
                change[20] += 1
                if change[10] > 0:
                    change[10] -= 1
                    change[5] -= 1
                else:
                    change[5] -= 3

            if change[5] < 0 or change[10] < 0: return False

        return True