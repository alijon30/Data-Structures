


You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:

An integer x - Record a new score of x.
"+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
"D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
"C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
Return the sum of all the scores on the record. The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
Example 2:

Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.


class Solution:
    def calPoints(self, ops: List[str]) -> int:

        stack = Stack()
        
        for i in ops:
            if i.isnumeric():
                stack.push(int(i))
            elif i == 'D':
                stack.push(2*stack.peek())
            elif i == "C":
                stack.pop()
            elif i == "+":
                a1 = stack.pop()
                a2 = stack.pop()
                stack.push(a2)
                stack.push(a1)
                stack.push(a1 + a2)
            elif i[0] == "-":
                stack.push(int(i))
        return stack.Sum()
        
        
class Stack:
    def __init__(self):
        self.list = []
    
    def isEmpty(self):
        if self.list == []: 
            return True
        else:
            return False

    def Sum(self):
        return sum(self.list)
    
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
          
          
          
    class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = Stack()
        
        for i in ops:
            if i.isnumeric():
                stack.push(int(i))
            elif i == "D":
                stack.push(2*stack.peek())
            elif i == "C":
                stack.pop()
            elif i[0] == "-":
                stack.push(int(i))
            elif i == "+":
                a1 = stack.pop()
                a2 = stack.pop()
                stack.push(a2)
                stack.push(a1)
                stack.push(a1 + a2)
        return stack.Sum()
        
        
        
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Linked:
    def __init__(self):
        self.head = None
class Stack:
    def __init__(self):
        self.linked = Linked()
    
    def Sum(self):
        node = self.linked.head
        target = 0
        while node:
            target += node.value
            node = node.next
        return target
    
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.linked.head
        self.linked.head = newNode
    
    def isEmpty(self):
        if self.linked.head == None:
            return True
        else:
            return False
    
    def pop(self):
        if self.isEmpty():
            return 
        else:
            nodeValue = self.linked.head.value
            self.linked.head = self.linked.head.next
            return nodeValue
    def peek(self):
        if self.isEmpty():
            return
        else:
            return self.linked.head.value
          
