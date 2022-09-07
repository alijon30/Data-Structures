Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

 

Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:


Input: root = [5,1,7]
Output: [1,null,5,null,7]




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        lst= []
        def InOrderTraversal(rootNode):
            if not rootNode:
                return
            InOrderTraversal(rootNode.left)
            lst.append(rootNode.val)
            InOrderTraversal(rootNode.right)
        InOrderTraversal(root)
        print(lst)
        def Insert(rootNode, NodeValue):
            customQueue = Queue()
            customQueue.enqueue(rootNode)
            while not customQueue.isEmpty():
                root = customQueue.dequeue()
                
                if root.value.right is None:
                    root.value.right = TreeNode(NodeValue)
                    return
                else:
                    customQueue.enqueue(root.value.right)
        newTree = TreeNode(lst[0])
        for i in range(1, len(lst)):
            Insert(newTree, lst[i])
            
        return newTree
class Node:
    def __init__(self, value):
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
        if self.linked.head is None:
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
            if self.linked.head == self.linked.tail:
                self.linked.head = None
                self.linked.tail = None
            else:
                self.linked.head = self.linked.head.next
            return node
          
          
          
