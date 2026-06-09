from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        elements=[]
        for i in range(len(nums)):
            count=0
            j=0
            while j<len(nums):
                if nums[i]>nums[j]:
                    count+=1
                j+=1
            elements.append(count)
        return elements
s=Solution()
print(s.smallerNumbersThanCurrent(nums = [8,1,2,2,3]))