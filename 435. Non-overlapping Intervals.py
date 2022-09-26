Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key= lambda x: x[0])
        counts = 0
        
        start = intervals[0][0]
        end = intervals[0][1]
        
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            
            if interval[0] < end:
                counts += 1
                start = max(start, interval[0])
                end = min(end , interval[1])
                
            else:
                start = interval[0]
                end = interval[1]
                
        
        return counts
        
        
        
        
