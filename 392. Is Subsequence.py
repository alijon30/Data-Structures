Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

  
  
  
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) <= len(t):
            stack1 = []

            for i in range(len(s)):
                stack1.append(s[i])

            stack2 = []
            j = 0
            while stack1 != []:
                while j != len(t):
                    if t[j] == stack1[0]:
                        stack1.pop(0)
                        stack2.append(t[j])
                    j += 1
                    if stack1 == []:
                        break
                if len(stack1) != 0:
                    return False

            if "".join(stack2) == s:
                return True
            else:
                return False
        else:
            return False
          
          
          
          
