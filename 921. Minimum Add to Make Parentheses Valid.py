A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

 

Example 1:

Input: s = "())"
Output: 1
Example 2:

Input: s = "((("
Output: 3

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = Stack()
        for i in range(len(s)):
            if stack.isEmpty():
                stack.push(s[i])
                
            else:
                if s[i] == ")":
                    if stack.peek() == "(":
                        stack.poop()
                    else:
                        stack.push(s[i])
                else:
                    stack.push(s[i])
        print(stack)
        return stack.Count()
        
class Stack:
    
    def __init__(self):
        self.list = []
        
    def __str__(self):
        return str(self.list)
    def Count(self):
        return len(self.list)
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def push(self, value):
        self.list.append(value)
        
    def poop(self):
        if self.isEmpty():
            return 
        else:
            self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return
        else:
            return self.list[-1]
          
