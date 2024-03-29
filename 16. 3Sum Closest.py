Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
Accepted
947.3K
Submissions
2.1M

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        min_dif = math.inf
        
        
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums)-1
            while left < right:
                current_diff = target - nums[i] - nums[left]-nums[right]

                if current_diff == 0:
                    return target

                if abs(min_dif) > abs(current_diff) or (abs(min_dif) == abs(current_diff) and current_diff>min_dif):
                    min_dif = current_diff


                if current_diff >0:
                    left += 1
                else:
                    right -=1
                                                    
        return target - min_dif
                                   
                                   
                                   
                                   
                                   
