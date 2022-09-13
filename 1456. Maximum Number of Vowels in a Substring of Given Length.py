Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_length = 0
        window_start = 0
        Vowels = ['a', 'e', 'i', 'o', 'u']
        counts = 0
        for window_end in range(len(s)):
            if s[window_end] in Vowels:
                counts += 1
                
            
            if window_end +1 > k:
                if s[window_start] in Vowels:
                    counts -= 1
                    
                window_start += 1
                
            max_length = max(max_length, counts)
            
        return max_length
      
      
      
      
