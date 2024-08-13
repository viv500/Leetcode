class Solution:
    def checkRecord(self, s: str) -> bool:
        late_streak = 0
        absent = 0

        for day in s:
            if day == "A":
                absent += 1
                late_streak = 0
                if absent >= 2:
                    return False
            elif day == "L":
                late_streak += 1
                if late_streak >= 3:
                    return False
            else:
                late_streak = 0

        return True
            
