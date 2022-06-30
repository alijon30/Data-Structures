Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        def LevelOrder(rootNode):
            if not rootNode:
                return
            else:
                customQueue = Queue()
                customQueue.enqueue(rootNode)
                
                while not customQueue.isEmpty():
                    root = customQueue.dequeue()
                    if root.value.val in range(low, high+1):
                        self.ans += root.value.val
                    
                    if root.value.left:
                        customQueue.enqueue(root.value.left)
                    
                    if root.value.right:
                        customQueue.enqueue(root.value.right)
        LevelOrder(root)
        return self.ans
                    
        
class Node:
    def __init__(self, value = None):   
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
class Queue:
    def __init__(self):
        self.linked = LinkedList()
    
    def isEmpty(self):
        if self.linked.head is None:
            return True
        else:
            return False
    
    def enqueue(self, NodeValue):
        newNode = Node(NodeValue)
        if self.isEmpty():
            self.linked.head = newNode
            self.linked.tail = newNode
        else:
            self.linked.tail.next = newNode
            self.linked.tail = newNode
    
    def dequeue(self):
        if self.isEmpty():
            return
        else:
            node = self.linked.head
            self.linked.head = self.linked.head.next
            return node
          
          
          
          
