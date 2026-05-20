from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix=[]
        s=0
        for i in nums:
            s+=i
            prefix.append(s)
        total=prefix[-1]
        for i in range(len(nums)):
            left_sum=0
            if i==0:
                left_sum=0
            else:
                left_sum=prefix[i-1]
            right_sum=total-prefix[i]
            if left_sum==right_sum:
                return i
        return -1
s = Solution()
print(s.pivotIndex([1,7,3,6,5,6]))