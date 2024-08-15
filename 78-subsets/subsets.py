class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        '''  
├── Include 1
│   ├── Include 2
│   │   ├── Include 3 (Subset: [1, 2, 3])
│   │   └── Exclude 3 (Subset: [1, 2])
│   └── Exclude 2
│       ├── Include 3 (Subset: [1, 3])
│       └── Exclude 3 (Subset: [1])
└── Exclude 1
    ├── Include 2
    │   ├── Include 3 (Subset: [2, 3])
    │   └── Exclude 3 (Subset: [2])
    └── Exclude 2
        ├── Include 3 (Subset: [3])
        └── Exclude 3 (Subset: []) '''

        subsets =[]

        def dfs(index, subset):

            if index >= len(nums):
                # creates a copy of subset and prevents previosly appended subsets to get affected
                # when we pop elements in the future
                subsets.append(subset[:])
                return


            # decision tree choice to include nums[i]
            subset.append(nums[index])
            dfs(index + 1, subset)

            # decision tree choice to exclude nums[i]
            subset.pop()
            dfs(index + 1, subset)

        
        # start of recursive call
        dfs(0, [])

        return subsets


            



        
