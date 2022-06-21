You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = Stack()
        stack.push(s[0])
        
        for i in s[1:]:
            if i == stack.peek():
                stack.pop()
            else:
                stack.push(i)
                
            
        return str(stack)
        
        
class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = [node for node in self.list]
        return "".join(values)
        
    def push(self, value):
        self.list.append(value)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return "The Stack is empty"
        else:
            return self.list[-1]
            
            
   class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = Stack()
        
        stack.push(s[0])
        
        for i in s[1:]:
            if i == stack.peek():
                stack.pop()
            else:
                stack.push(i)
        
        return str(stack)[::-1]

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
class Stack:
    def __init__(self):
        self.linkedList = Linkedlist()
        
    def __str__(self):
        values = [node.value for node in self.linkedList]
        return "".join(values)
    
    def push(self, value):
        NodeValue = Node(value)
        NodeValue.next = self.linkedList.head
        self.linkedList.head = NodeValue
    
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            node = self.linkedList.head
            self.linkedList.head = self.linkedList.head.next
            return node.value
    
    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            
            return self.linkedList.head.value
        
        
        
