A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strin = ""
        
        for letter in s:
            if ( 65 <= ord(letter) <= 90):
                strin += chr(ord(letter) + 32)
                
            elif (97 <= ord(letter) <= 122) or (48 <= ord(letter) <= 57):
                strin += letter
        print(strin)
        return True if strin == strin[::-1] else False
      
      
      
