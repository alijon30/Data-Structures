

class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        
        for i in s:
            if stack.isEmpty():
                stack.push(i)
            else:
                if i == ")" and stack.peek() == "(":
                    stack.pop()
                elif i == "]" and stack.peek() == "[":
                    stack.pop()
                elif i == "}" and stack.peek() == "{":
                    stack.pop()
                else:
                    stack.push(i)
        if stack.Size() == 0:
            return True
        else:
            return False
        
                    
        
        
class Stack:
    def __init__(self):
        self.list = []
    
    def Size(self):
        return len(self.list)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def push(self, value):
        self.list.append(value)
    
    def pop(self):
        if self.isEmpty():
            return
        else:
            return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return
        else:
            return self.list[-1]
          
          
