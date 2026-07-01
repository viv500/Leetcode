class Solution:
    def candy(self, ratings: List[int]) -> int:

        # left increasing sequence and right icnreaing sequence
        # as long as neighbors are increasing, canadies will also need to be increaign (from either side)
        # pick the max candy value at each position between left and right

        # icnreasing sequence resets to 1 when theres a decrease
        
        left_increasing = [1] * len(ratings)
        right_increasing = [1]* len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]: left_increasing[i] = left_increasing[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]: right_increasing[i] = right_increasing[i + 1] + 1

        candy = 0
        for i in range(len(ratings)):
            candy += max(left_increasing[i], right_increasing[i])
            
        return candy


        