class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        # Pair jobs and sort by difficulty
        # can scan left to right to find the highest profit at a given difficulty
        jobs = sorted(zip(difficulty, profit))

        # Precompute the running maximum profit at each difficulty
        max_profit_at_diff = []
        max_so_far = 0
        for d, p in jobs:
            max_so_far = max(max_so_far, p)
            max_profit_at_diff.append((d, max_so_far))
        
        print(max_profit_at_diff)

        # Sort workers: improves 2 pointer efficiency
        worker.sort()

        # Two-pointer approach
        total = 0
        j = 0
        n = len(jobs)

        # 2 pointer efficient here cuz pointer stays at same spot for next worker since its sorted
        for ability in worker:
            while j < n and jobs[j][0] <= ability:
                j += 1
            if j > 0:
                total += max_profit_at_diff[j - 1][1] # the job right before the difficulty was too hard
                

        return total
