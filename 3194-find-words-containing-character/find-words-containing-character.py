from typing import List
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        index=len(words)-1
        result=set([])
        while index>-1:
            if x in words[index]:
                result.add(index)
            index-=1
        return list(result)
s=Solution()
print(s.findWordsContaining(words = ["abc","bcd","aaaa","cbc"], x = "z"))