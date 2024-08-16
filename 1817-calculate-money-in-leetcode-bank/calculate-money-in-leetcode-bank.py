class Solution:
    def totalMoney(self, n: int) -> int:
        start = 0
        week = 0
        total = 0

        for i in range(1, n + 1):
            if i % 7 == 0:
                # add normally for the 7th day
                start += 1
                total += start

                week += 1

                # reset count
                start = week
            else:
                start += 1
                total += start
        
        return total 
        