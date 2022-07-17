Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = Heap(len(nums))
        for i in nums:
            heap.Insert(i)
        
        print(heap.customList)
        
        while k != 1:
            heap.Delete()
            k -= 1
            
        return heap.peek()
        
class Heap:
    def __init__(self, size):
        self.HeapSize = 0
        self.customList = [None] * (size + 1)
        
        
    def peek(self):
        if self.HeapSize == 0:
            return
        return self.customList[1]
        
    def Heapify(self, index):
        parent_index = int(index/2)
        
        if index <= 1:
            return
        
        if self.customList[index] > self.customList[parent_index]:
            self.customList[index], self.customList[parent_index] = self.customList[parent_index], self.customList[index]
            
        self.Heapify(parent_index)
        
    def Insert(self, Value):
        self.customList[self.HeapSize + 1] = Value
        self.HeapSize += 1
        self.Heapify(self.HeapSize)
        
    def Extractor(self, index):
        left = index * 2
        right = index * 2 + 1
        swap  =0
        
        if self.HeapSize < left:
            return
        elif self.HeapSize == left:
            if self.customList[left] > self.customList[index]:
                self.customList[left], self.customList[index] = self.customList[index], self.customList[left]
                
            return
        else:
            if self.customList[left] > self.customList[right]:
                swap = left
            else:
                swap = right
            if self.customList[index] < self.customList[swap]:
                self.customList[index], self.customList[swap] = self.customList[swap], self.customList[index]
                
            self.Extractor(swap)
            
    def Delete(self):
        if self.HeapSize == 0:
            return
        self.customList[1] = self.customList[self.HeapSize]
        self.customList[self.HeapSize] = None
        self.HeapSize -= 1
        self.Extractor(1)
