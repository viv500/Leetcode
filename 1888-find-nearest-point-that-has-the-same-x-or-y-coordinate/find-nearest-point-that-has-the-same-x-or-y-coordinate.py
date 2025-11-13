class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """

        smallest = float('inf')
        smallest_index = 0

        for index, point in enumerate(points):
            if point[0] == x or point[1] == y:
                man = abs(x - point[0]) + abs(y - point[1])
                if man < smallest:
                    smallest = man
                    smallest_index = index

        return -1 if smallest == float('inf') else smallest_index

        
        