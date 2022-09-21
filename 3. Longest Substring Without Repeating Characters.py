Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_index_freq = {}
        window_start = 0
        max_length = 0
        for window_end in range(len(s)):
            current = s[window_end]
            
            if current not in char_index_freq:
                char_index_freq[current] = window_end
            else:
                window_start = max(window_start, char_index_freq[current] + 1)
                char_index_freq[current] = window_end
            max_length = max(max_length, window_end - window_start + 1)
            
        return max_length
        
        
        
