class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1=set(nums1)
        s2=set(nums2)
        s3=set(nums3)
        result=[]
        for i in s1|s2|s3:
            count=0
            if i in s1:
                count+=1
            if i in s2:
                count+=1
            if i in s3:
                count+=1
            if count>=2:
                result.append(i)
        return result
