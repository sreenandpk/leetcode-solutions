class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""

        for i in range(0, len(s), 2 * k):

            rev = ""

            # reverse first k characters
            for j in range(min(i + k - 1, len(s) - 1), i - 1, -1):
                rev += s[j]

            # keep next k characters same
            normal = ""

            for j in range(i + k, min(i + 2 * k, len(s))):
                normal += s[j]

            result += rev + normal

        return result


s = Solution()
print(s.reverseStr("abcdefg", 2))