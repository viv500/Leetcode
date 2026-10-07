from collections import defaultdict
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:

        count_gaps = defaultdict(int)

        for layer in wall:
            pos = 0
            for cut in layer[:-1]:
                pos += cut
                count_gaps[pos] += 1
                
        return len(wall) - max(count_gaps.values(), default=0)