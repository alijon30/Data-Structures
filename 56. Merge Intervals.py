Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
Accepted
1,652,143
Submissions


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        merged = []
        
        intervals.sort(key= lambda x : x[0])
        
        start = intervals[0][0]
        end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            
            if interval[0] <= end:
                start = min(interval[0], start)
                end = max(interval[1], end)
                
            else:
                merged.append([start, end])
                start = interval[0]
                end = interval[1]
                
        
        merged.append([start, end])
        return merged
