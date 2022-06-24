Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

 

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        def Merge(left, right):
            i = 0 
            j = 0
            
            res = []
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            
            while i < len(left):
                res.append(left[i])
                i += 1
            
            while j < len(right):
                res.append(right[j])
                j += 1
            
            return res
        def MergeSort(array):
            n = len(array)
            if n <= 1:
                return array
            
            Left = MergeSort(array[:round(n/2)])
            Right = MergeSort(array[round(n/2):])
            
            return Merge(Left, Right)
        
        sorted_list = MergeSort(nums)
        
        res = []
        
        curr = -99
        ind = -99
        
        for Index, Value in enumerate(nums):
            nums[Index] = sorted_list.index(Value)
            
        return nums
      
      
      
