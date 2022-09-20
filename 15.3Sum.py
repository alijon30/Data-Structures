Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        
        
        def find_pairs(array, first, first_sum , triplets):
            left = first + 1
            right = len(array) - 1
            print("Inside")
            while left < right:
                current_sum = array[left] + array[right]
                
                
                if current_sum == first_sum:
                    lst = [-first_sum, array[left], array[right]]
                    if lst not in triplets:
                        triplets.append(lst)
                    left += 1
                    right -= 1
                    
                    while left < right and array[left] == array[left-1]:
                        left += 1
                        
                    while left < right and array[right] == array[right+1]:
                        right -= 1
                
                elif current_sum > first_sum:
                    right -= 1
                
                else:
                    left += 1
                
                
        
        
        
        nums.sort()
        print(nums)
        for i in range(len(nums)-2):
            if nums[i] > 0 and nums[i] == nums[i-1]:
                continue
            find_pairs(nums, i, -nums[i], triplets)
            print(i)
            
        return triplets
      
      
      
