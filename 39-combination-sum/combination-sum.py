class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # Naive approach:
        # Build a decision tree where each candidate is a branch choice at every step.
        # This leads to duplicate combinations.

        # Better approach:
        # At each index, decide whether to INCLUDE the current candidate
        # (and stay on the same index since we can reuse it),
        # or EXCLUDE it (and move to the next index).

        '''[]
├── [2]
│   ├── [2,2]
│   │   ├── [2,2,2]
│   │   │   └── X
│   │   └── [2,2,3]   <-- valid
│   └── [2]
│       ├── [2,3]     X
│       └── [2]
│           ├── X
│           └── X
└── []
    ├── [3]
    └── []
        ├── [6]
        └── []
            ├── [7]   <-- valid
            └── []    (no solution)'''

        result = []

        def dfs(i, cur, total):
            # Base cases:
            # Out of bounds OR sum exceeded target → stop exploring
            if i >= len(candidates) or total > target:
                return

            # Found a valid combination
            if total == target:
                result.append(cur.copy())
                return

            # INCLUDE current candidate (stay at same index)
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # BACKTRACK and try EXCLUDING current candidate
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return result

        # Time Complexity: O(2^n * k)
        # - Each element has two choices (include/exclude) → exponential recursion tree
        # - k = average length of a valid combination (cost of copying)

        # Space Complexity: O(k)
        # - Recursion stack + current path (excluding output list)