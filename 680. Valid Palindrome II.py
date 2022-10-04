Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        
        while left < right:
            
            if s[left] != s[right]:
                skipL, skipR = s[left+1: right + 1], s[left: right]
                
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            
            left += 1
            right -= 1
        
        return True
        
        
        
        
