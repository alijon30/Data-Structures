In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a new word "another".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

 

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        trie = Trie()
         
        res = []
        
        for word in dictionary:
            trie.Insert(word)
        print(words)
        for i in range(len(words)):
            temp = "".join(trie.Search(words[i]))
            if temp:
                words[i] = temp
        
        return " ".join(words)
            
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []
        self.endOfString = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.similarities = 0
    def Insert(self, word):
        current = self.root
        
        for let in word:
            if let not in current.children:
                current.children[let] = TrieNode()
            current = current.children[let]
        
        current.words.append(word)
        current.endOfString = True
        
    def Search(self, word):
        current = self.root
        self.similarities = 0
        for let in word:
            if let not in current.children:
                break
            if current.endOfString == True:
                return current.words
            current = current.children[let]
            self.similarities += 1
        
        if self.similarities < len(current.words):
            return []
        
        return current.words
      
      
      
