An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.

Given an integer n, return true if n is strictly palindromic and false otherwise.

A string is palindromic if it reads the same forward and backward.

 

Example 1:

Input: n = 9
Output: false
Explanation: In base 2: 9 = 1001 (base 2), which is palindromic.
In base 3: 9 = 100 (base 3), which is not palindromic.
Therefore, 9 is not strictly palindromic so we return false.
Note that in bases 4, 5, 6, and 7, n = 9 is also not palindromic.
Example 2:

Input: n = 4
Output: false
Explanation: We only consider base 2: 4 = 100 (base 2), which is not palindromic.
Therefore, we return false.




class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        pointer = False
        
        
        
        def base_string_repr(num, base):
            lst = []
            while num // base == 0:
                integer_part = num / base
                fraction_part = num % base
                lst.append(str(fraction_part))
                num //= base
                
            return True if lst == lst[::-1] else False
        
        
        
        for i in range(2, n-1):
            pointer = base_string_repr(n, i)
            if pointer is not True:
                return pointer
        
        
