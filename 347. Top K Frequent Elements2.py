Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Dict= {}
        for val in nums:
            if val not in Dict:
                Dict[val] = 0
            Dict[val] += 1
        
        heap = Heap(len(Dict))
        for key, value in Dict.items():
            heap.HeapifyInsert([key, value])
        
        res = []
        while k != 0:
            res.append(heap.Extract()[0])
            k -= 1
        
        return res
            
        
        
class Heap:
    def __init__(self, size):
        self.HeapSize = 0
        self.customList = [None] * (size + 1)
        
    def Heapify(self, index):
        parent_index = int(index/2)
        
        if index <= 1:
            return
        
        if self.customList[index][1] > self.customList[parent_index][1]:
            self.customList[index], self.customList[parent_index] = self.customList[parent_index], self.customList[index]
        
        return self.Heapify(parent_index)
    
    def HeapifyInsert(self, value):
        
        self.customList[self.HeapSize+1] = value
        self.HeapSize += 1
        self.Heapify(self.HeapSize)
        
    def Extractor(self, index):
        leftIndex = index * 2
        rightIndex = index * 2 + 1
        swap = 0 
        
        if self.HeapSize < leftIndex:
            return 
        elif self.HeapSize == leftIndex:
            if self.customList[index][1] < self.customList[leftIndex][1]:
                self.customList[index], self.customList[leftIndex] = self.customList[leftIndex], self.customList[index]
                
        else:
            if self.customList[leftIndex][1] > self.customList[rightIndex][1]:
                swap = leftIndex
            else:
                swap = rightIndex
            if self.customList[index][1] < self.customList[swap][1]:
                self.customList[index], self.customList[swap] = self.customList[swap], self.customList[index]
            
            self.Extractor(swap)
    
    def Extract(self):
        extracted = self.customList[1]
        self.customList[1] = self.customList[self.HeapSize]
        self.HeapSize -= 1
        self.Extractor(1)
        return extracted
        
