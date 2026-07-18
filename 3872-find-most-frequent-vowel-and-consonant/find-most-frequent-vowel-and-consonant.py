class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels="aeiou"
        v={}
        not_v={}
        for i in s:
            if i in vowels:
                if i in v:
                    v[i]+=1
                else:
                    v[i]=1
            else:
                if i in not_v:
                    not_v[i]+=1
                else:
                    not_v[i]=1
        
        v_max= max(v.values(),default=0)
        not_v_max=max(not_v.values(),default=0)
        return v_max+not_v_max
s=Solution()
print(s.maxFreqSum(s = "successes"))