Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105



class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window_start = 0
        
        num_freq_ind = {}
        
        for window_end in range(len(nums)):
            current = nums[window_end]
            
            if current not in num_freq_ind:
                num_freq_ind[current] = window_end
            else:
                
                if window_end - num_freq_ind[current] <= k:
                    return True
                num_freq_ind[current] = window_end
        return False
                
                
                
