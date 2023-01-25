Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
Accepted
613.8K
Submissions
1.3M
Acceptance Rate
46.2%



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        queue = deque()
        queue.append(root)
        exists = False
        while queue:
            currentLevel = len(queue)

            for _ in range(currentLevel):
                node = queue.popleft()
                if node.val == subRoot.val:
                    exists = self.check_trees(node, subRoot)
                    if exists:
                        return True
                if node.left :
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return False
    
    def check_trees(self, root1, root2):
        if not root1 and not root2:
            return True
        if root1 and root2 and root1.val == root2.val:
            return self.check_trees(root1.left, root2.left) and self.check_trees(root1.right, root2.right)
        return False
        
        
        
