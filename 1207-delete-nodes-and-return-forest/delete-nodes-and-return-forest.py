# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        result = []
        
        to_delete = set(to_delete)

        def dfs(node, isRoot):
            if not node: return None
            delete = node.val in to_delete

            node.left = dfs(node.left, delete)
            node.right = dfs(node.right, delete)
    
            if isRoot and not delete: result.append(node)
            
            return None if delete else node


        dfs(root, True)

        return result


