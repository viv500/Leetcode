class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        line = []
        for p, f, t in trips:
            line.append([f, p])
            line.append([t, -p])
        
        line.sort()

        total = 0
        for _, count in line:
            total += count
            if total > capacity: return False

        return True