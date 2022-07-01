Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.list = []
        
        def PreOrderTraversal(rootNode):
            if not rootNode:
                return
            
            self.list.append(rootNode.val)
            PreOrderTraversal(rootNode.left)
            PreOrderTraversal(rootNode.right)
            
        def InOrderTraversal(rootNode):
            if not rootNode:
                return
            InOrderTraversal(rootNode.left)
            self.list.append(rootNode.val)
            InOrderTraversal(rootNode.right)
            
        def PostOrderTraversal(rootNode):
            if not rootNode:
                return
            
            PostOrderTraversal(rootNode.left)
            PostOrderTraversal(rootNode.right)
            self.list.append(rootNode.val)
        
        PostOrderTraversal(root)
    
            
        print(self.list)
        return sorted(self.list)[k-1]
