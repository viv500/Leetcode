class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        

        # naive approach to solve this is to create a decision tree with each option from candidate as a branch
        # this however, would lead to duplicate sum arrays

        # better approach: decision tree where each decision is "Include this candidate or nah" and it will make this decision recrusively for each element in the array


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
            # no way to make it work, return
            if i >= len(candidates) or total > target:
                return

            if total == target:
                result.append(cur.copy())
                return


            # the "include" branch
            cur.append(candidates[i])
            
            dfs(i, cur, total + candidates[i])

            # backtracking - the "exclude" branch
            cur.pop()

            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        
        return result
            
            