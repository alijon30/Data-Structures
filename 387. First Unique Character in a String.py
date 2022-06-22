

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        Dict1 = {}
        
        
        for ind, val in enumerate(s):
            if val not in Dict1.keys():
                Dict1[val] = ind
            else:
                Dict1[val] = -999
        
        for val, ind in Dict1.items():
            if ind != -999:
                return ind
        
        return -1
      
      
