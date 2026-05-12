from typing import List
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        length=len(words)
        for i in words:
            ok=True
            while count<=length:
                if len(i)==1:
                    if i in allowed:
                        count+=1
                    break
                if len(i)>1:
                    for j in i:
                        if j not in allowed:
                            ok=False
                            break
                    if ok:
                        count+=1
                    break
        return count
s=Solution()
print(s.countConsistentStrings(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]))