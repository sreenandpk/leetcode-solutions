class Solution:
    def reverseWords(self, s: str) -> str:
        rev=""
        og=""
        for i in range(len(s)-1,-1,-1):
            rev+=s[i]
        s_rev=rev.split()
        for i in range(len(s_rev)-1,-1,-1):
            og+=s_rev[i]+" "
        return og.strip()
s=Solution()
print(s.reverseWords("Let's take LeetCode contest"))