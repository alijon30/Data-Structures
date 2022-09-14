The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:

It has a length of k.
It is a divisor of num.
Given integers num and k, return the k-beauty of num.

Note:

Leading zeros are allowed.
0 is not a divisor of any value.
A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: num = 240, k = 2
Output: 2
Explanation: The following are the substrings of num of length k:
- "24" from "240": 24 is a divisor of 240.
- "40" from "240": 40 is a divisor of 240.
Therefore, the k-beauty is 2.
Example 2:

Input: num = 430043, k = 2
Output: 2
Explanation: The following are the substrings of num of length k:
- "43" from "430043": 43 is a divisor of 430043.
- "30" from "430043": 30 is not a divisor of 430043.
- "00" from "430043": 0 is not a divisor of 430043.
- "04" from "430043": 4 is not a divisor of 430043.
- "43" from "430043": 43 is a divisor of 430043.
Therefore, the k-beauty is 2.



class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        window_start = 0
        counts = 0
        sub_num = ""
        str_num = str(num)
        
        for window_end in range(len(str_num)):
            sub_num += str_num[window_end]
            
            if len(sub_num) == k:
                try:
                    if num % int(sub_num) == 0:
                        counts += 1
                except ZeroDivisionError:
                    pass

            if len(sub_num) == k:
                if k == 1:
                    sub_num = ""
                else:
                    sub_num = sub_num[1:]
                
                
        return counts
      
      
