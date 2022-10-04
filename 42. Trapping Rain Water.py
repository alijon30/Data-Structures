Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        res = 0
        
        leftMax, rightMax = height[left], height[right]
        
        while left < right:
            
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]
            else:
                right -= 1
                rightMax= max(rightMax, height[right])
                res += rightMax - height[right]
                
        return res
        
        
        
        
