You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

 

Example 1:


Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
Example 2:


Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.array= []
        def InOrderTraversal(rootNode):
            if not rootNode:
                return
            
            
            InOrderTraversal(rootNode.left)
            self.array.append(rootNode)
            InOrderTraversal(rootNode.right)
            
        InOrderTraversal(root)
        srt = sorted(v.val for v in self.array)
        
        for i in range(len(srt)):
            self.array[i].val = srt[i]
            
            
            
