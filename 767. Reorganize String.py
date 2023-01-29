Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.



class Solution:
    def reorganizeString(self, s: str) -> str:
        
        char_frequency = {}

        for let in s:
            char_frequency[let] = char_frequency.get(let, 0) + 1

        self.heap = []

        for char, frequency in char_frequency.items():
            heappush(self.heap, (-frequency, char))


        previous, previous_freq = None, 0
        result = []

        while self.heap:
            frequency, char = heappop(self.heap)

            if previous and -previous_freq > 0:
                heappush(self.heap, (previous_freq, previous))

            result.append(char)
            previous = char
            previous_freq = frequency + 1

        return ''.join(result) if len(result) == len(s) else ''


