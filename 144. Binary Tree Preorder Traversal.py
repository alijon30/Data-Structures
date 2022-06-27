Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        def PreOrderTraversal(rootNode):
            if not rootNode:
                return
            lst.append(rootNode.val)
            PreOrderTraversal(rootNode.left)
            PreOrderTraversal(rootNode.right)
        
        PreOrderTraversal(root)
        return lst
      
      
