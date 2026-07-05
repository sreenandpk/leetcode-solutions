
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        nums=str(nums)
        result=[]
        for i in nums:
            if i.isdigit():
                result.append(int(i))
        return result

