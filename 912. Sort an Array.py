Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        
        def Merge(L, R):
            nums = []
            i = 0
            j = 0
            
            
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    nums.append(L[i])
                    i += 1
                else:
                    nums.append(R[j])
                    j += 1
            
            while i <len(L):
                nums.append(L[i])
                i += 1
            
            while j < len(R):
                nums.append(R[j])
                j += 1
                
            return nums
            
            
        
        def MergeSort(array):
            n = len(array)
            
            if n <= 1:
                return array
            
            left = MergeSort(array[round(n/2):])
            right = MergeSort(array[:round(n/2)])
            return Merge(left, right)
    
        srt = MergeSort(nums)
        return srt
      
      
      
      
