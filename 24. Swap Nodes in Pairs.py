Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = tail = ListNode()
        lst = []
        
        while head:
            lst.append(head.val)
            head = head.next
        
        length = int(len(lst)/2)
        while length !=0:
            a = length * 2-1
            lst[a], lst[a-1] = lst[a-1], lst[a]
            
            length -= 1
        
        for val in lst:
            tail.next = ListNode(val)
            tail= tail.next
        
        return dummy.next
        
