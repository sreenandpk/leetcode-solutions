class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            n=str(n)
            l=[0]
            for i in n:
                sq=int(i)*int(i)
                l.append(l[-1]+sq)
            n=l[-1]
        return True
s=Solution()
print(s.isHappy(n = 19))