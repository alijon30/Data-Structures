Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]



class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
            
        def binary_search(nums, target, FindMax):
            keyIndex = -1
            
            start, end = 0, len(nums)-1
            
            while start <= end:
                middle = start + (end-start)//2
                
                if nums[middle] < target:
                    start = middle + 1
                
                elif nums[middle] > target:
                    end = middle - 1
                    
                else:
                    keyIndex = middle
                    if FindMax:
                        start = middle + 1
                    else:
                        end = middle - 1
                        
            return keyIndex
        
        result = [-1, -1]
        
        result[0] = binary_search(nums, target, False)
        
        if result[0] != -1:
            result[1] = binary_search(nums, target, True)
        return result
        
        
        
        
