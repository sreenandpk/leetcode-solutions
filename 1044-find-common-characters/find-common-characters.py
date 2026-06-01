from typing import List
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result=[]
        for i in words[0]:
            count=0
            for j in words:
                if i in j:
                    count+=1
            if count==len(words):
                result.append(i)
                for d in range(len(words)):
                    words[d]=words[d].replace(i,"",1)
        return result
s=Solution()
print(s.commonChars(words = ["bella","label","roller"]))