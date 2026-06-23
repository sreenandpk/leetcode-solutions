class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        index=len(nums)-1
        for i in range(len(nums),2*len(nums)):
            nums.append(nums[index])
            index-=1
        return nums
s=Solution()
print(s.concatWithReverse( nums = [1,2,3]))