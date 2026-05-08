class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Brute force would try every starting index: O(n^2)
        # Greedy approach below: O(n)

        # If total cost exceeds total gas, no solution exists
        if sum(cost) > sum(gas): return -1

        # A solution is guaranteed to exist from here on
        diff = [g - c for g, c in zip(gas, cost)]

        # Key insight: if the running total goes negative at index i,
        # then no starting point in [start, i] can complete the circuit.
        # So we reset and try starting from i + 1.
        # Since a solution is guaranteed, the final starting_index must be valid.

        running_total, starting_index = 0, 0

        for index, amount in enumerate(diff):
            running_total += amount
            if running_total < 0:
                running_total = 0
                starting_index = index + 1 
                # dont need to modulo wrap wround index cuz if it WAS 0, then "starting_index" would've never changed from 0

        return starting_index