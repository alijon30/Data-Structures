Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.





class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        length = len(points)
        heap = Heap(length)
        for l in points:
            heap.Insert(l)
            
        res = []
        
        while k != 0:
            res.append(heap.peek())
            heap.Extract()
            k -= 1
        
        return res
        
        
        
        
        
        
        
class Heap:
    def __init__(self, size):
        self.HeapSize = 0
        self.MaxSize = size + 1
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
        if self.customList[index][0] * self.customList[index][0] + self.customList[index][1] * self.customList[index][1] < self.customList[parent_index][0] * self.customList[parent_index][0] + self.customList[parent_index][1]*self.customList[parent_index][1]:
            self.customList[index], self.customList[parent_index] = self.customList[parent_index], self.customList[index]
            
        self.Heapify(parent_index)
    
    def Insert(self, Value):
        if self.HeapSize + 1 == self.MaxSize:
            return
        self.customList[self.HeapSize + 1] = Value
        self.HeapSize += 1
        self.Heapify(self.HeapSize)
        
    def HeapifyExtractor(self, index):
        leftIndex = index * 2
        rightIndex = index * 2 +1
        swap = 0
        
        if self.HeapSize < leftIndex:
            return
        elif self.HeapSize == leftIndex:
            if self.customList[index][0] * self.customList[index][0] + self.customList[index][1]*self.customList[index][1] > self.customList[leftIndex][0] * self.customList[leftIndex][0] + self.customList[leftIndex][1] * self.customList[leftIndex][1]:
                self.customList[index], self.customList[leftIndex] = self.customList[leftIndex], self.customList[index]
            return
        else:
            if self.customList[leftIndex][0] * self.customList[leftIndex][0] + self.customList[leftIndex][1] * self.customList[leftIndex][1] < self.customList[rightIndex][0] * self.customList[rightIndex][0] + self.customList[rightIndex][1]*self.customList[rightIndex][1]:
                swap = leftIndex
            else:
                swap = rightIndex
            if self.customList[index][0] * self.customList[index][0] + self.customList[index][1]*self.customList[index][1] > self.customList[swap][0] * self.customList[swap][0] + self.customList[swap][1] * self.customList[swap][1]:
                self.customList[index], self.customList[swap] = self.customList[swap], self.customList[index]
            
            self.HeapifyExtractor(swap)
    
    def Extract(self):
        if self.HeapSize == 0:
            return
        ret = self.customList[1]
        self.customList[1] = self.customList[self.HeapSize]
        self.customList[self.HeapSize] = None
        self.HeapSize -= 1
        self.HeapifyExtractor(1)
        return ret
        
        
        
