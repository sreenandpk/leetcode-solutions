class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=set(['a','e','i','o','u'])
        count=0
        for i in range(k):
            if s[i] in vowels:
                count+=1
        maximum=count
        for j in range(k,len(s)):
            if s[j-k] in vowels:
                count-=1
            if s[j] in vowels:
                count+=1
            maximum=max(count,maximum)
        return maximum
s=Solution()
print(s.maxVowels(s = "abciiidef", k = 3))