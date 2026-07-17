class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:

            # Remove bigger previous digits while we still can
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        # If removals are still left, remove from the end
        while k > 0:
            stack.pop()
            k -= 1

        # Convert list to string
        ans = "".join(stack)

        # Remove leading zeros
        ans = ans.lstrip("0")

        return ans if ans else "0"


s = Solution()
print(s.removeKdigits(num="1432219", k=3))