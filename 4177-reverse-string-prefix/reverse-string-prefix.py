class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        new=""
        rev=""
        for i in range(len(s)):
            if i==k:
                break
            else:
                new+=s[i]
        for i in range(len(new)-1,-1,-1):
            rev+=new[i]
                
        for i in range(len(s)):
            if i>=k:
                rev+=s[i]
        return rev
s=Solution()
print(s.reversePrefix(s = "abcd", k = 2))