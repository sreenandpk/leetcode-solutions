from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        elements={}
        for i in nums:
            if i in elements:
                elements[i]+=1
            else:
                elements[i]=1
        single=[]
        for _,value in elements.items():
            if value==1:
                single.append(_)
        return single
s=Solution()
print(s.singleNumber(nums = [1,2,1,3,2,5]))