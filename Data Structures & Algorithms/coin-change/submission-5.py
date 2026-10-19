class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amounts = [float("inf")] * (amount + 1)
        amounts[0] = 0

        for a in range(amount + 1):
            for c in coins:
                if a - c >= 0:
                    amounts[a] = min(amounts[a], 1 + amounts[a - c])

        
        return amounts[amount] if amounts[amount] != float("inf") else -1
        