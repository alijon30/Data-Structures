Given the root of a binary tree, return the sum of values of its deepest leaves.
 

Example 1:


Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        queue = [(1, root)]
        max_depth = 0
        res = 0
        
        while len(queue) > 0:
            depth , node = queue.pop(0)
            
            if depth > max_depth:
                max_depth = depth
                res = node.val
            elif depth == max_depth:
                res += node.val
                
            for child in (node.left, node.right):
                if child:
                    queue.append((depth+1, child))
            
        return res
