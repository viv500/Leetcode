# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# at any node, number of moves is given by the abs(size of subtree - coins)
# cuz a node having a surplus of x coins needs to make x moves in sending out those coins
class Solution:
    def distributeCoins(self, root: TreeNode | None) -> int:
        moves = 0
        def dfs(node):
            nonlocal moves
            if not node: return [0, 0] # [size, number of coins]

            left_size, left_coins = dfs(node.left)
            right_size, right_coins = dfs(node.right)

            size = 1 + left_size + right_size
            coins = node.val + left_coins + right_coins

            moves += abs(size - coins)
            return [size, coins]

        dfs(root)
        return moves



