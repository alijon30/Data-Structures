Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_start = 0
        char_freq = {}
        
        
        for letter in p:
            if letter not in char_freq:
                char_freq[letter] = 0
            char_freq[letter] += 1
            
            
        array = []
        matches = 0
        
        
        for window_end in range(len(s)):
            current = s[window_end]
            
            if current in char_freq:
                char_freq[current] -= 1
                
                if char_freq[current] == 0:
                    matches += 1
            
            if matches == len(char_freq):
                array.append(window_start)
            
            if window_end >= len(p)-1:
                left = s[window_start]
                window_start += 1
                if left in char_freq:
                    if char_freq[left] == 0:
                        matches -=1
                    char_freq[left] += 1
                    
                    
        return array
