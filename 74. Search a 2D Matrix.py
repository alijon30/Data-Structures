You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row, col = len(matrix), len(matrix[0])

        top, bot = 0, row-1

        while top <= bot:

            mid = (top + bot)//2

            if matrix[mid][0] > target:
                bot = mid - 1
            
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break

        start, end = 0, col-1
        mid = (top + bot)//2
        while start <= end:
            m = start + (end-start)//2

            if matrix[mid][m] > target:
                end = m - 1
            elif matrix[mid][m] < target:
                start = m + 1
            else:
                return True
        return False
        
        
        
