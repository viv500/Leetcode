# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# NOTE: dont use 2 * i + 1 and 2 * i + 2 logic: the in order traveral doesn't produce null children for null nodes in the string
#  tree [1,null,3,4,5,6,7] produces [1,null,3,6,7]
# ex. 1N34567NNNNNN is wrong, but 1N3NN45NNNN67NNNNNN is correct 


# root=[1,null,3,4,5,6,7] would be null left child, 4 and 5 are 3's children, 6 and 7 are 3s children. no other nulls
# null doesn't have child nulls

from collections import deque
class Codec:

    
    # in order traversal using bfs

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        code = ""

        q = deque([(root)])

        while q:
            for _ in range(len(q)):
                child = q.popleft()

                # is not None
                if child:
                    code += str(child.val)
                    code += "#" # need a delimiter for double digit numbers
                    q.append(child.left)
                    q.append(child.right)
                else:
                    code += "N"
                    code += "#" # delimiter


        # ex. 123NN45NNNN
        # ex. 1N34567NNNNNN
        print(code)
        return code



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "N#": return None
        data = [token for token in data.split("#") if token] # to avoid the "" at the end, which would error int("")


        index = 0
        root = TreeNode(val=data[index])
        q = deque([root])

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node is None: continue

                index += 1
                if index >= len(data) or data[index] in "N":
                    node.left = None
                else:
                    node.left = TreeNode(val = int(data[index]))

                index += 1
                if index >= len(data) or data[index] == "N":
                    node.right = None
                else:
                    node.right = TreeNode(val = int(data[index]))


                q.append(node.left)    
                q.append(node.right)





        return root



        # DOESNT WORK !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # node: i, left child: 2 * i + 1, right child: 2 * i + 2
        # parameters represent the index of node in the in-order representation
        def construct(root, left, right):
            if root >= len(data) or data[root] == "N": return

            node = TreeNode(val=data[root])

            left_child = 2 * root + 1
            right_child = 2 * root + 2
        

            node.left = construct(left_child, left_child * 2 + 1, left_child * 2 + 2)
            node.right = construct(right_child, right_child * 2 + 1, right_child * 2 + 1)

            return node

        return construct(0, 1, 2) # this will return the node for 0
