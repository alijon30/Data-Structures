You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.

In one operation:

choose an index i such that 0 <= i < nums.length,
increase your score by nums[i], and
replace nums[i] with ceil(nums[i] / 3).
Return the maximum possible score you can attain after applying exactly k operations.

The ceiling function ceil(val) is the least integer greater than or equal to val.

 

Example 1:

Input: nums = [10,10,10,10,10], k = 5
Output: 50
Explanation: Apply the operation to each array element exactly once. The final score is 10 + 10 + 10 + 10 + 10 = 50.
Example 2:

Input: nums = [1,10,3,3,3], k = 3
Output: 17
Explanation: You can do the following operations:
Operation 1: Select i = 1, so nums becomes [1,4,3,3,3]. Your score increases by 10.
Operation 2: Select i = 1, so nums becomes [1,2,3,3,3]. Your score increases by 4.
Operation 3: Select i = 2, so nums becomes [1,1,1,3,3]. Your score increases by 3.
The final score is 10 + 4 + 3 = 17.



from heapq import *
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # here I would like to get max scores so what about implementing priority queue
        
        heap = []
        
        for num in nums:
            heappush(heap, -num)
            
        ans = 0
        
        for i in range(k):
            removed = heap[0]
            self.remove(heap, removed)
            ans += removed * (-1)
            heappush(heap, math.floor(removed/3))
        
        return ans
    def remove(self, heap, element):
        ind = heap.index(element)  # find the element
        # copy the last element of the heap to this index and decrement the heap size
        heap[ind] = heap[-1]
        del heap[-1]

        # adjust the position of the element while maintaining the heap property.
        # we can use heapify to readjust the elements but that would be O(N),
        # instead, we will adjust only one element which will O(logN)
        if ind < len(heap):
          heapq._siftup(heap, ind)
          heapq._siftdown(heap, 0, ind)
          
          
          
          
