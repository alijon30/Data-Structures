
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        reversed1= None
        first = l1
        
        while first:
            nxt = first.next
            first.next = reversed1
            reversed1 = first
            first = nxt
        
        reversed2 = None
        second = l2
        
        while second:
            nxt = second.next
            second.next = reversed2
            reversed2 = second
            second = nxt
        child = 0
        dummy = ListNode()
        tail = dummy
        while reversed1 and reversed2:
            addition = reversed1.val + reversed2.val + child
            if addition >= 10:
                child = 1
                addition -= 10
            else:
                child = 0
            tail.next = ListNode(addition)
            tail = tail.next
            reversed1 = reversed1.next
            reversed2 = reversed2.next
        
        while reversed1:
            addition = reversed1.val + child
            if addition >= 10:
                addition -= 10
                child = 1
            else:
                child = 0
            tail.next = ListNode(addition)
            tail = tail.next
            reversed1 = reversed1.next
        
        while reversed2:
            addition = reversed2.val + child
            if addition >= 10:
                addition -= 10
                child = 1
            else:
                child = 0
            tail.next = ListNode(addition)
            tail = tail.next
            reversed2 = reversed2.next
        if child == 1:
            tail.next = ListNode(1)
            tail = tail.next
        prev = None
        curr = dummy.next
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
      
      
