Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        trie = Trie()
        
        for num in range(1, n+1):
            trie.Insert(str(num))
        res = trie.print_num(trie.root, '')
        return res
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.numbers = []
        
    def Insert(self, word):
        current = self.root
        
        for l in word:
            if l not in current.children:
                current.children[l] = TrieNode()
            current = current.children[l]
            
        current.endOfString = True
    
    def print_num(self, c_node, cs):
        if c_node.endOfString:
            self.numbers.append(int(cs))
            
        for num, node in c_node.children.items():
            self.print_num(node, cs + num)
            
        return self.numbers
    
