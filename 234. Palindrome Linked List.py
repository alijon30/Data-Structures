Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        
        while head:
            lst.append(head.val)
            head = head.next
            
        mid = len(lst)/2
        
        if len(lst) % 2 == 0:
            mid = len(lst) // 2
            first = lst[:mid]
            second = lst[mid:]
        else:
            mid = len(lst) // 2 + 1
            first = lst[:mid-1]
            second = lst[mid:]
    
        if first == second[::-1]:
            return True
        else:
            return False
          
