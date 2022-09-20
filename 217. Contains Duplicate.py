Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        
        char_frequency = {}
        
        for i in nums:
            if i not in char_frequency:
                char_frequency[i] = 0
                
            char_frequency[i] += 1
            
            
        if len(char_frequency) != length:
            return True
        else:
            return False
