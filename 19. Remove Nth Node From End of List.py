Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        _new = head
        previous = None
        length = 0
        next = None
        while _new is not None:
            length += 1
            _new = _new.next
        current = head
        print(length)
        if length <= n and head.next is None:
            head = None
            return head
        elif length - n == 0:
            current = current.next
            return current
        i = 1
        next = None
        while current is not None and length - n > i:
            i += 1
            current = current.next
        print(i)   
        print(current)
        
        current.next = current.next.next
        
        while current is not None:
            current = current.next
        print(length)
        return head
        
        
