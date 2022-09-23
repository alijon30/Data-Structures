Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).



class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        window_Sum = 0
        min_length = math.inf
        window_start = 0
        
        
        for window_end in range(len(nums)):
            current = nums[window_end]
            window_Sum += current
            
            
            
            while window_Sum >= target:
                
                min_length = min(min_length, window_end - window_start + 1)
                left = nums[window_start]
                window_Sum -= left
                window_start += 1
                
                
            
        if min_length != math.inf:
            return min_length
        else:
            return 0
          
          
          
