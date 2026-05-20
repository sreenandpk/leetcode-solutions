class NumArray:
    def __init__(self,nums):
        self.prefix=[]
        s=0
        for i in nums:
            s+=i
            self.prefix.append(s)
    def sumRange(self,left,right):
        if left==0:
            return self.prefix[right]
        return self.prefix[right]-self.prefix[left-1]
s=NumArray([1,2,3,4])
print(s.sumRange(1,2))
        