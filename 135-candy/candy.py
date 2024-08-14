class Solution:
    def candy(self, ratings: List[int]) -> int:
        # core: 2 passes, from left and right, to ensure accurate distribution

        n = len(ratings)

        # mininmum number of candies per child
        distribute = [1] * n

        # left pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                # not just incrementing by 1, but incrementing by 1 more than neighbour
                distribute[i] += distribute[i - 1]

        # right pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                # we want to minimize the number of extra candies we give out. if the current amount is enough
                # keep it that way. if not, make it 1 more than its neighbour
                distribute[i] = max(distribute[i], distribute[i + 1] + 1)

        return sum(distribute)

        
        



