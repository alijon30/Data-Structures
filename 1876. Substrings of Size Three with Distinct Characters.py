A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".
Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        max_length = 0
        window_start = 0
        char_frequency = {}
        
        for window_end in range(len(s)):
            right_char = s[window_end]
            
            if right_char not in char_frequency:
                char_frequency[right_char] = 0
            char_frequency[right_char] += 1
            
            
            if window_end >= 2:
                left_char = s[window_start]
                if len(char_frequency) == 3:
                    max_length += 1
                    print(char_frequency)
                window_start += 1
                char_frequency[left_char] -= 1
                
                if char_frequency[left_char] == 0:
                    del char_frequency[left_char]
        return max_length
      
      
      
