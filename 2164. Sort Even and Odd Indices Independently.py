You are given a 0-indexed integer array nums. Rearrange the values of nums according to the following rules:

Sort the values at odd indices of nums in non-increasing order.
For example, if nums = [4,1,2,3] before this step, it becomes [4,3,2,1] after. The values at odd indices 1 and 3 are sorted in non-increasing order.
Sort the values at even indices of nums in non-decreasing order.
For example, if nums = [4,1,2,3] before this step, it becomes [2,1,4,3] after. The values at even indices 0 and 2 are sorted in non-decreasing order.
Return the array formed after rearranging the values of nums.

 

Example 1:

Input: nums = [4,1,2,3]
Output: [2,3,4,1]
Explanation: 
First, we sort the values present at odd indices (1 and 3) in non-increasing order.
So, nums changes from [4,1,2,3] to [4,3,2,1].
Next, we sort the values present at even indices (0 and 2) in non-decreasing order.
So, nums changes from [4,1,2,3] to [2,3,4,1].
Thus, the array formed after rearranging the values is [2,3,4,1].
Example 2:

Input: nums = [2,1]
Output: [2,1]
Explanation: 
Since there is exactly one odd index and one even index, no rearrangement of values takes place.
The resultant array formed is [2,1], which is the same as the initial array. 

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        odd_array = []
        even_array = []
        
        for el in range(len(nums)):
            if el % 2 == 0:
                even_array.append(nums[el])
            else:
                odd_array.append(nums[el])
                
        
        def Merge(Left, Right):
            l = 0
            r = 0
            nums = []
            
            while l < len(Left) and r < len(Right):
                if Left[l] <= Right[r]:
                    nums.append(Left[l])
                    l += 1
                else:
                    nums.append(Right[r])
                    r += 1
                    
            
            while l < len(Left):
                nums.append(Left[l])
                l += 1
            
            while r < len(Right):
                nums.append(Right[r])
                r += 1
            return nums
        
        def MergeSort(array):
            n = len(array)
            if n <= 1:
                return array
            
            Left = MergeSort(array[round(n/2):])
            Right = MergeSort(array[:round(n/2)])
            
            return Merge(Left, Right)
    
        odd_array = MergeSort(odd_array)[::-1]
        even_array = MergeSort(even_array)
        newList = []
        
        while even_array != [] and odd_array != []:
            newList.append(even_array.pop(0))
            newList.append(odd_array.pop(0))
        
        while even_array != []:
            newList.append(even_array.pop(0))
        
        while odd_array != []:
            newList.append(odd_array.pop(0))
        
        return newList
      
      
      
      
