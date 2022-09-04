Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

A grandparent of a node is the parent of its parent if it exists.

 

Example 1:


Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        queue = Queue()
        parent = 0
        children = 0
        items = []
        def LevelOrderTraversal(rootNode, parent, children):
            if not rootNode:
                return
            customQueue = Queue()
            customQueue.enqueue(rootNode)
            while not customQueue.isEmpty():
                root = customQueue.dequeue()
                if root.value.val % 2 == 0:
                    if root.value.left is not None:
                        el = root.value.left
                        if el.left is not None:
                            print(el.left.val)
                            items.append(el.left.val)
                        if el.right is not None:
                            items.append(el.right.val)
                    if root.value.right is not None:
                        el = root.value.right
                        if el.left is not None:
                            items.append(el.left.val)
                        if el.right is not None:
                            items.append(el.right.val)
                if root.value.left is not None:
                    customQueue.enqueue(root.value.left)
                
                if root.value.right is not None:
                    customQueue.enqueue(root.value.right)
        LevelOrderTraversal(root, parent, children)
        return sum(items)
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
    
    def __str__(self):
        values = [str(value) for value in self.linked]
        return ' '.join(values)
    
    def enqueue(self, NodeValue):
        newNode = Node(NodeValue)
        if self.linked.head is None:
            self.linked.head = newNode
            self.linked.tail = newNode
        else:
            self.linked.tail.next = newNode
            self.linked.tail = newNode
    
    def isEmpty(self):
        if self.linked.head is None:
            return True
        else:
            return False
    
    def dequeue(self):
        if self.isEmpty():
            return "Empty"
        else:
            node = self.linked.head
            if self.linked.head == self.linked.tail:
                self.linked.head = None
                self.linked.tail = None
            else:
                self.linked.head = self.linked.head.next
            return node
            
            
            
