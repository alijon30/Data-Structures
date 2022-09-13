Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        max_length = 0
        window_start = 0
        char_frequency = {}
        
        for window_end in range(len(s)):
            right_char = s[window_end]
            
            if right_char not in char_frequency:
                char_frequency[right_char] = 0
            
            char_frequency[right_char] += 1
            
            while len(char_frequency) == 3:
                max_length += len(s) - window_end
            
                left_char = s[window_start]
            
                if left_char in char_frequency:
                    char_frequency[left_char] -= 1
                    if char_frequency[left_char] == 0:
                        del char_frequency[left_char]
                
                window_start += 1
            
        return max_length
      
      
      
      
