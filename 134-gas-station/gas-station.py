class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(cost) > sum(gas):
            return -1

        diff = []

        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])

        total = 0
        start_index = 0

        for i in range(len(diff)):

            total += diff[i]

            if total < 0:
                # that start index didnt work, reset total and try next index
                total = 0
                start_index = i + 1

            # if you kept adding to total and it never became negative, that start index worked

        return start_index
        