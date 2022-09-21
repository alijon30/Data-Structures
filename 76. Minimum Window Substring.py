Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
        char_freq = {}
        
        
        for letter in t:
            if letter not in char_freq:
                char_freq[letter] = 0
            char_freq[letter] += 1
            
        
        window_start = 0
        matched = 0
        min_length = len(s) + 1
        substr_start = 0
        for window_end in range(len(s)):
            current = s[window_end]
            
            if current in char_freq:
                char_freq[current] -= 1
                
                if char_freq[current] >= 0:
                    matched += 1
                    
            
            while matched == len(t):
                
                if min_length > window_end - window_start + 1:
                    min_length = window_end - window_start + 1
                    substr_start = window_start
                    
                    
                left_char = s[window_start]
                window_start += 1
                
                if left_char in char_freq:
                    if char_freq[left_char] == 0:
                        matched -= 1
                    char_freq[left_char] += 1
        if min_length > len(s):
            return ""
        return s[substr_start: min_length + substr_start]
        
        
