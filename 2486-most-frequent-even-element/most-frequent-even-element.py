from typing  import  List
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            if i%2==0:
                freq[i]=freq.get(i,0)+1
        if not freq:
            return -1
        ans=min(freq.keys())
        for k,count in freq.items():
            if count>freq[ans]:
                ans=k
            elif count==freq[ans] and k<ans:
                ans=k
        return ans
s=Solution()
print(s.mostFrequentEven(nums = [0,1,2,1]))