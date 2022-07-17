Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

class Solution:
    def frequencySort(self, s: str) -> str:
        
        Dict = {}
        
        for let in s:
            if let not in Dict:
                Dict[let] = 1
            else:
                Dict[let] += 1
        heap = Heap(len(Dict.keys()))
        for let, count in Dict.items():
            heap.Insert([count, let])
        
        return heap.LevelOrder()
        
        
class Heap:
    def __init__(self, size):
        self.HeapSize = 0
        self.MaxSize = size +1
        self.customList = [None] * (size + 1)
    
    def LevelOrder(self):
        string = ""
        if self.HeapSize == 0:
            return
        else:
            while self.HeapSize != 0:
                string += self.customList[1][0] * self.customList[1][1]
                self.Delete()
            return string
                
    
    def peek(self):
        if self.HeapSize == 0:
            return
        else:
            return self.customList[1]
        
    def Heapify(self, index):
        parent_index = int(index/2)
        
        if index <= 1:
            return
        
        if self.customList[parent_index][0] < self.customList[index][0]:
            self.customList[parent_index], self.customList[index] = self.customList[index], self.customList[parent_index]
            
        self.Heapify(parent_index)
        
    def Insert(self, Value):
        if self.HeapSize + 1 == self.MaxSize:
            return
        self.customList[self.HeapSize + 1] = Value
        self.HeapSize += 1
        self.Heapify(self.HeapSize)
        
    def Extractor(self, index):
        leftChild = index * 2
        rightChild = index * 2 + 1
        swap = 0
        
        if self.HeapSize < leftChild:
            return
        elif self.HeapSize == leftChild:
            if self.customList[leftChild][0] > self.customList[index][0]:
                self.customList[leftChild], self.customList[index] = self.customList[index], self.customList[leftChild]
                
            return
        else:
            if self.customList[leftChild][0] > self.customList[rightChild][0]:
                swap = leftChild
            else:
                swap = rightChild
            if self.customList[index][0] < self.customList[swap][0]:
                self.customList[index], self.customList[swap] = self.customList[swap], self.customList[index]
            self.Extractor(swap)
            
    def Delete(self):
        if self.HeapSize == 0:
            return
        self.customList[1] = self.customList[self.HeapSize]
        self.customList[self.HeapSize] = None
        self.HeapSize -= 1
        self.Extractor(1)
    
