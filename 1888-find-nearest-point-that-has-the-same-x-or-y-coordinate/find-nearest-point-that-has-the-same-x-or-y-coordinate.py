class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        smallest_distance = float('inf')
        smallest_index = float('inf')

        for index, point in enumerate(points):
            x1, y1 = point
            distance = abs(x1 - x) + abs(y1 - y)

            if distance < smallest_distance and (x1 == x or y1 == y):
                smallest_distance = distance
                smallest_index = index

        return -1 if smallest_index == float('inf') else smallest_index