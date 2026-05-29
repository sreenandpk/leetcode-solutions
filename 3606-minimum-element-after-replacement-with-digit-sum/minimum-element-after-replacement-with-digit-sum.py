from typing import List
class Solution:
    def minElement(self, nums: List[int]) -> int:
        prefix=[]
        s=0
        for i in  nums:
            for j in str(i):
                s+=int(j)
            prefix.append(s)
            s=0
        minimum=prefix[0]
        for m in prefix:
            if m<minimum:
                minimum=m
        return minimum
s=Solution()
print(s.minElement(nums = [10,12,13,14]))