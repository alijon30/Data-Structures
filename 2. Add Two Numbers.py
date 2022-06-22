

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        child = 0
        while l1 and l2:
            addition = l1.val + l2.val
            if child == 1:
                addition += 1
                if addition >= 10:
                    addition -= 10
                    child = 1
                else:
                    child = 0
            if addition >= 10:
                child = 1
                addition -= 10
            tail.next = ListNode(addition)
            l1 = l1.next
            l2 = l2.next
            tail = tail.next
        while l1:
            a = l1.val + child
            if a >= 10:
                a -= 10
                child = 1
            else:
                child = 0
            tail.next = ListNode(a)
            l1 = l1.next
            tail = tail.next
        
        while l2:
            a = l2.val + child
            if a >= 10:
                a -= 10
                child = 1
            else:
                child = 0
            tail.next = ListNode(a)
            l2 = l2.next
            tail = tail.next
        if child == 1:
            tail.next = ListNode(1)
            tail = tail.next
        return dummy.next
      
      
