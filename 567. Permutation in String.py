Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_freq = {}
        window_start = 0
        
        for char in s1:
            if char not in char_freq:
                char_freq[char] = 0
            char_freq[char] += 1
            
        matched = 0
        
        for window_end in range(len(s2)):
            current_char = s2[window_end]
            
            if current_char in char_freq:
                char_freq[current_char] -= 1
                
                if char_freq[current_char] == 0:
                    matched += 1
                    
            if matched == len(char_freq):
                return True
            
            if window_end >= len(s1)-1:
                left = s2[window_start]
                window_start += 1
                
                if left in char_freq:
                    if char_freq[left] == 0:
                        matched -= 1
                    char_freq[left] += 1
                    
        return False
        
        
        
