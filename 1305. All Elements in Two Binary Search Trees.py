Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

 

Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:


Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res1 = []
        res2 = []
        def Traversal(rootNode, lst):
            if not rootNode:
                return None
            else:
                custom = Queue()
                custom.enqueue(rootNode)
                
                while not custom.isEmpty():
                    root = custom.dequeue()
                    lst.append(root.data.val)
                    
                    if root.data.left:
                        custom.enqueue(root.data.left)
                    if root.data.right:
                        custom.enqueue(root.data.right)
            return lst
        Traversal(root1, res1)
        Traversal(root2, res2)
        res1.extend(res2)
        
        def Merge(left, right):
            i = 0
            j = 0
            
            result = []
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j+= 1
            while i < len(left):
                result.append(left[i])
                i += 1
            while j < len(right):
                result.append(right[j])
                j += 1
            return result
        def MergeSort(nums):
            n = len(nums)
            if n <= 1:
                return nums
            left = MergeSort(nums[:round(n/2)])
            right = MergeSort(nums[round(n/2):])
            return Merge(left, right)
        res1 = MergeSort(res1)
        return res1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
class Queue:
    def __init__(self):
        self.linked = LinkedList()
    
    def enqueue(self, date):
        newNode = Node(date)
        
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
            return 
        else:
            node = self.linked.head
            
            if self.linked.head == self.linked.tail:
                self.linked.head = None
                self.linked.tail = None
            else:
                self.linked.head = self.linked.head.next
            return node
    
