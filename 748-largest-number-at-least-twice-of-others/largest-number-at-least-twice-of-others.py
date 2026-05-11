from typing import List
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest=max(nums)
        index=nums.index(largest)
        for i in nums:
            if i!=largest and largest <i*2:
                return -1
        return index
s=Solution()
print(s.dominantIndex([3,6,1,0]))