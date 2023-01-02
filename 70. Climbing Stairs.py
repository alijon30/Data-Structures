You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def helper(num, dp):
            if num == 2:
                return 2
            if num == 1:
                return 1
            if num in dp:
                return dp[num]
            else:
                takeOne = helper(num-1, dp)
                takeTwo = helper(num-2, dp)
                dp[num] = takeOne + takeTwo
                return dp[num]
        return helper(n, dp)
        
        
        
        
