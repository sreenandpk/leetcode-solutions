from typing import List
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left=0
        right=0
        left_prefix=[]
        right_prefix=[]
        for i in range(len(nums)):
            left_prefix.append(left)
            left+=nums[i]
        for j in range(len(nums)-1,-1,-1):
            right_prefix.append(right)
            right+=nums[j]
        result=[]
        left=0
        right=len(right_prefix)-1
        while right>=0:
            if left_prefix[left]>right_prefix[right]:
                result.append(left_prefix[left]-right_prefix[right])
            else:
                result.append(right_prefix[right]-left_prefix[left])
            left+=1
            right-=1
        return result
s=Solution()
print(s.leftRightDifference(nums = [10,4,8,3]))