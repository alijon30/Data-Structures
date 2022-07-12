Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        forms = collections.Counter(words)
        heap = Heap(len(forms.keys()))
        
        for el, count in forms.items():
            heap.Insert([count, el])
        
        res = []
        while k != 0:
            res.append(heap.peek()[1])
            k -= 1
            heap.Delete()
        return res
        
        
class Heap:
    def __init__(self, size):
        self.MaxSize = size + 1
        self.HeapSize = 0
        self.customList = [None] * (size + 1)
        
    def peek(self):
        if self.HeapSize == 0:
            return
        else:
            return self.customList[1]
        
    def Heapify(self, index):
        parent_index = int(index/2)
        if index <= 1:
            return
        
        if self.customList[index][0] > self.customList[parent_index][0]:
            self.customList[index], self.customList[parent_index] = self.customList[parent_index], self.customList[index]
        
        elif self.customList[index][0] == self.customList[parent_index][0]:
            first = sorted([self.customList[index][1], self.customList[parent_index][1]])[0]
            second = sorted([self.customList[index][1], self.customList[parent_index][1]])[1]
            
            self.customList[parent_index][1] = first
            self.customList[index][1] = second
            
        self.Heapify(parent_index)
    
    def Insert(self, Value):
        if self.HeapSize + 1 == self.MaxSize:
            return
        self.customList[self.HeapSize + 1] = Value
        self.HeapSize += 1
        self.Heapify(self.HeapSize)
        
    def HeapifyExtractor(self, index):
        leftChild = index * 2
        rightChild = index * 2 + 1
        swap = 0
        
        if self.HeapSize < leftChild:
            return
        elif self.HeapSize == leftChild:
            if self.customList[index][0] < self.customList[leftChild][0]:
                self.customList[index], self.customList[leftChild] = self.customList[leftChild], self.customList[index]
            
            elif self.customList[index][0] == self.customList[leftChild][0]:
                sorted_str = sorted([self.customList[index][1], self.customList[leftChild][1]])
                self.customList[index][1] = sorted_str[0]
                self.customList[leftChild][1] = sorted_str[1]
        else:
            if self.customList[leftChild][0] > self.customList[rightChild][0]:
                swap = leftChild
            elif self.customList[leftChild][0] == self.customList[rightChild][0]:
                sorted_str = sorted([self.customList[leftChild][1], self.customList[rightChild][1]])
                if sorted_str[0] == self.customList[leftChild][1]:
                    swap = leftChild
                else:
                    swap = rightChild
            else:
                swap = rightChild
            
            if self.customList[index][0] < self.customList[swap][0]:
                self.customList[index], self.customList[swap] = self.customList[swap], self.customList[index]
            
            elif self.customList[index][0] == self.customList[swap][0]:
                sorted_str = sorted([self.customList[index][1], self.customList[swap][1]])
                self.customList[index][1] = sorted_str[0]
                self.customList[swap][1] = sorted_str[1]
            self.HeapifyExtractor(swap)
            
    def Delete(self):
        if self.HeapSize == 0:
            return
        self.customList[1] = self.customList[self.HeapSize]
        self.customList[self.HeapSize] = None
        self.HeapSize -= 1
        self.HeapifyExtractor(1)
        
