class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num=list(num)
        for i in range(len(num)-1,-1,-1):
            if num[i]=="0":
                num.pop()
            else:
                break
        return "".join(num)
s=Solution()
print(s.removeTrailingZeros(num = "51230100"))