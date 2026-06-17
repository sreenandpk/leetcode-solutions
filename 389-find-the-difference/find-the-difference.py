class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ele={}
        for i in s:
            ele[i]=ele.get(i,0)+1
        for j in t:
            ele[j]=ele.get(j,0)-1
        for k,v in ele.items():
            if v!=0:
                return k
s=Solution()
print(s.findTheDifference(s = "a", t = "aaa"))