A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        elif len(nums) == 2:
            return nums.index(max(nums))
        queue = Queue()
        q = 0
        for i in range(len(nums)-1):
            if queue.isEmpty():
                queue.Insert(nums[i])
            
            if nums[i] > queue.peek() and nums[i] > nums[i+1]:
                return i
            
            queue.Insert(nums[i])
        if q == 0:
            return nums.index(max(nums))
        
        
class Queue:
    def __init__(self):
        self.customList = []
        
    def isEmpty(self):
        if self.customList == []:
            return True
        else:
            return False

    def peek(self):
        if self.isEmpty():
            return 
        else:
            return self.customList[-1]
        
    def Insert(self, value):
        self.customList.append(value)
        
        
        
