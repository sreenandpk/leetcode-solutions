from typing import List
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        largest=[]
        for i in range(len(sentences)):
            largest.append(len(sentences[i].split()))
        return max(largest)
s=Solution()
print(s.mostWordsFound(sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))