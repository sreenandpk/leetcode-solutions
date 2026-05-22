from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        minimum = float('inf')
        for right in range(len(nums)):
            # Expand window
            current_sum += nums[right]
            # Shrink window while condition satisfied
            while current_sum >= target:
                minimum = min(minimum, right - left + 1)
                current_sum -= nums[left]
                left += 1
        if minimum == float('inf'):
            return 0
        return minimum
s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))