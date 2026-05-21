from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum=0
        for i in range(k):
            window_sum+=nums[i]
        maximum=window_sum
        for i in range(k,len(nums)):
            window_sum-=nums[i-k]
            window_sum+=nums[i]
            maximum=max(maximum,window_sum)
        return maximum/k
s = Solution()
print(s.findMaxAverage([1,12,-5,-6,50,3], 4))