
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        #Time Complexity of the following sliding window algorithm is O(N)
        #Space Complexity is O(1)
        
        
        max_length = 0
        char_freq = {}
        window_start = 0
        
        max_characters = 0
        for window_end in range(len(s)):
            current = s[window_end]
            
            if current not in char_freq:
                char_freq[current] = 0
            char_freq[current] += 1
            
            max_characters = max(max_characters, char_freq[current])
            
            if window_end - window_start + 1 - max_characters > k:
                left = s[window_start]
                window_start += 1
                char_freq[left] -= 1
                
            max_length = max(max_length, window_end - window_start + 1)
            
        return max_length
        
        
