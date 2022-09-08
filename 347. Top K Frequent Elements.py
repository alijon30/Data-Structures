Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        length = len(set(nums))
        heap = Heap(length)
        self.ans = []
        for values, counts in counter.items():
            heap.HeapifyInsert([values, counts])
            print(f"{values} -> {counts}")
        print(heap.customList)
        while k != 0:
            ans = heap.Extract()[0]
            print("Ya")
            self.ans.append(ans)
            k -= 1
        return self.ans
        
        
class Heap:
    def __init__(self, size):
        self.HeapSize = 0
        self.customList = [None] * (size + 1)
        
    def peek(self):
        if self.customList == []:
            return
        else:
            return self.customList[1]
        
    def Traverse(self):
        for i in range(1, self.HeapSize + 1):
            print(self.customList[i])
            
    def Heapify(self, index):
        parent_index = int(index/2)
        
        if index <= 1:
            return
        
        if self.customList[index][1] > self.customList[parent_index][1]:
            self.customList[index], self.customList[parent_index] = self.customList[parent_index], self.customList[index]
            
        self.Heapify(parent_index)
        
    
    def HeapifyInsert(self, Value):
        self.customList[self.HeapSize+1] = Value
        self.HeapSize += 1
        self.Heapify(self.HeapSize)
        
    
    def Extractor(self, index):
        leftChild = index * 2
        rightChild = index * 2 + 1
        swapChild = 0
        
        if self.HeapSize < leftChild:
            return
        elif self.HeapSize == leftChild:
            if self.customList[index][1] < self.customList[leftChild][1]:
                self.customList[index], self.customList[leftChild] = self.customList[leftChild], self.customList[index]
            return
        else:
            if self.customList[leftChild][1] > self.customList[rightChild][1]:
                swapChild = leftChild
            else:
                swapChild = rightChild
            
            if self.customList[index][1] < self.customList[swapChild][1]:
                self.customList[index], self.customList[swapChild] = self.customList[swapChild], self.customList[index]
            
            self.Extractor(swapChild)
    def Extract(self):
        extracted_node = self.customList[1]
        self.customList[1] = self.customList[self.HeapSize]
        self.customList[self.HeapSize] = None
        self.HeapSize -= 1
        self.Extractor(1)
        return extracted_node
        
