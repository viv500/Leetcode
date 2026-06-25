class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1

        diff = [gas[i] - cost[i] for i in range(len(cost))]
        
        start = 0
        cur_sum = 0

        for index, val in enumerate(diff):
            cur_sum += val
            if cur_sum < 0: 
                cur_sum = 0
                start = index + 1

        return start