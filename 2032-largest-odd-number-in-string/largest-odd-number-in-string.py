class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                ans = ""
                for j in range(i + 1):
                    ans += num[j]
                return ans
        return ""

s = Solution()
print(s.largestOddNumber("35427"))