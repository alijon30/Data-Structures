Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
 

Example 1:

Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
Example 3:

Input: nums = [3,7]
Output: 12

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        self.product = 1
        length = len(nums)
        newHeap = Heap(length)
        for i in nums:
            newHeap.Insert(i)
        
        self.product = (newHeap.peek())-1
        newHeap.Extract()
        self.product = self.product * (newHeap.peek()-1)
        return self.product
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
        
        if self.customList[index] > self.customList[parent_index]:
            self.customList[index], self.customList[parent_index] = self.customList[parent_index], self.customList[index]
            
        self.Heapify(parent_index)
        
    def Insert(self, Value):
        if self.HeapSize + 1 == self.MaxSize:
            return "Full"
        else:
            self.customList[self.HeapSize + 1] = Value
            self.HeapSize += 1
            self.Heapify(self.HeapSize)
    def HeapifyExtract(self, index):
        leftChild = index * 2
        rightChild = index * 2 + 1
        swapChild= 0
        
        if self.HeapSize < leftChild:
            return
        elif self.HeapSize == leftChild:
            if self.customList[index] < self.customList[leftChild]:
                self.customList[index], self.customList[leftChild] = self.customList[leftChild], self.customList[index]
                
            return
        else:
            if self.customList[leftChild] > self.customList[rightChild]:
                swapChild = leftChild
            else:
                swapChild = rightChild
            
            if self.customList[index] < self.customList[swapChild]:
                self.customList[index], self.customList[swapChild] = self.customList[swapChild], self.customList[index]
            self.HeapifyExtract(swapChild)
        
        
    def Extract(self):
        if self.HeapSize == 0:
            return
        else:
            self.customList[1] = self.customList[self.HeapSize]
            self.customList[self.HeapSize] = None
            self.HeapSize -= 1
            self.HeapifyExtract(1)
            
            
            
