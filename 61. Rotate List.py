Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None or head.next is None or k <= 0:
            return head

        length = 1
        cur = head

        while cur.next is not None:
            length += 1
            cur = cur.next

        rotations = k % length
        ind = length - rotations
        cur.next = head
        last_node = head
        for i in range(ind-1):
            last_node = last_node.next
        head = last_node.next
        last_node.next = None
        return head




