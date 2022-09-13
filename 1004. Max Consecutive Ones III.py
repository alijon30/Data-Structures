Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0
        window_start = 0
        max_1s_count = 0
        
        
        for window_end in range(len(nums)):
            if nums[window_end] == 1:
                max_1s_count += 1
                
            
            if window_end - window_start + 1 - max_1s_count > k:
                if nums[window_start] == 1:
                    max_1s_count -= 1
                    
                window_start += 1
            
            max_length = max(max_length, window_end - window_start + 1)
            
        return max_length
      
      
