# time is O(n) space is O(h) for recursive stack but this code leaves in 0-values keys
# for O(h) space, use get() method and delete a key if its value goes to 0
# note: prefix is a global dictionary so need to decrement in the "backtrack" step
# runningSum makes a local copy at each step so that value gets restored anywhere
# dont need to decrement it
from collections import defaultdict
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        count = 0
        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(node, runningSum):
            nonlocal count
            if not node: return

            runningSum += node.val
            print('running sum: ', runningSum)
            count += prefix[runningSum - targetSum]

            prefix[runningSum] += 1

            dfs(node.left, runningSum)
            dfs(node.right, runningSum)

            prefix[runningSum] -= 1

        dfs(root, 0)
        print(prefix)
        return count