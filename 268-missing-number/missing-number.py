
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maximum=nums[0]
        minimum=nums[0]
        for i in nums:
            if i >maximum:
                maximum=i
            if i<minimum:
                minimum=i
        for i in range(minimum,maximum+1):
            if i not in nums:
                return i
        if minimum > 0:
            return 0 
        return maximum + 1    
s=Solution()
print(s.missingNumber(nums = [3,0,1]))