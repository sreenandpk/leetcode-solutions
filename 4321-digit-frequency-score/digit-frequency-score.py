class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        n=str(n)
        seen=set()
        ans=0
        for i in range(len(n)):
            if int(n[i]) in seen:
                    continue
            count=0
            right=len(n)-1
            while right>=0:
                if int(n[i])==int(n[right]):
                    count+=1
                right-=1
            seen.add(int(n[i]))
            ans += int(n[i]) * count
        return ans
s=Solution()
print(s.digitFrequencyScore(n = 122))