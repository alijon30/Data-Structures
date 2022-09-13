Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

 

Example 1:

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
Example 2:

Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        window_start = 0
        window_sum = 0
        max_length = 0
        
        for window_end in range(len(arr)):
            window_sum += arr[window_end]
            
            if window_end >= k-1:
                left_char = arr[window_start]
                window_start += 1
                
                if window_sum/k >= threshold:
                    max_length += 1
                
                window_sum -= left_char
                
        return max_length
      
      
