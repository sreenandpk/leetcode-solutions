class Solution:
    def clearDigits(self, s: str) -> str:
        result=[]
        for i in s:
            if i.isdigit():
                result.pop()
            else:
                result.append(i)
        return "".join(result)
s=Solution()
print(s.clearDigits(s = "abc"))