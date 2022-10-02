Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
Accepted
655,594
Submissions
1,791,113



class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        lst = []
        
        def find_pairs(nums, first, second, target, lst):
            left = second + 1
            right = len(nums)-1
            
            while left < right:
                current_Sum = nums[first] + nums[second] + nums[left] + nums[right]
                
                if current_Sum == target:
                    lst.append([nums[first], nums[second], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -=1
                elif current_Sum > target:
                    right -= 1
                else:
                    left += 1
                    
        
        
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            for j in range(i + 1,len(nums)-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                find_pairs(nums, i, j, target, lst)
                
        return lst
        
        
        
