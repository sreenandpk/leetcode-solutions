class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        ele={}
        for i in nums:
            if i%2==0:
               ele[i]=ele.get(i,0)+1
        minimum=[]
        for _,val in ele.items():
            if val==1:
                minimum.append(_)
        if minimum:
            return minimum[0]
        else:
            return -1
s=Solution()
print(s.firstUniqueEven(nums = [4,4]))