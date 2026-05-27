class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        longest=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack)==0:
                    stack.append(i)
                else:
                    length=i-stack[-1]
                    longest=max(longest,length)
        return longest
s=Solution()
print(s.longestValidParentheses(s = "(()"))