
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_frequency = {}
        matches = 0
        for letter in t:
            if letter not in char_frequency:
                char_frequency[letter] = 0
            char_frequency[letter] += 1
        print(char_frequency)
        for char in s:
            print(char)
            if char in char_frequency:
                matches += 1
                char_frequency[char] -= 1
            
                if char_frequency[char] == 0:
                    del char_frequency[char]
            else:
                matches -= 1
        
        if matches == len(t):
            return True
        else:
            return False
            
            
            
