from typing import List
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for ch in ".,!?;:'":
            paragraph=paragraph.replace(ch," ")
        d={}
        for i in paragraph.split():
            i=i.lower()
            if i not in banned:
                if i in d:
                    d[i]+=1
                else:
                    d[i]=1
        common=""
        maximum=0
        for k,v in d.items():
            if v>maximum:
                maximum=v
                common=k
        return common
s=Solution()
print(s.mostCommonWord(paragraph = "a.", banned = []))