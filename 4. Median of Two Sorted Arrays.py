Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.




class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge(left, right):
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
        
        merged = merge(nums1, nums2)
        mid = len(merged)/2
        print(mid)
        if len(merged) % 2 != 0:
            return merged[int(mid)]
        else:
            return (merged[int(mid)-1] + merged[int(mid)])/2
        
        
        
        
