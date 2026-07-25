class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for length in range(1, n // 2 + 1):

            if n % length != 0:
                continue

            valid = True

            for i in range(n):
                if s[i] != s[i % length]:
                    valid = False
                    break

            if valid:
                return True

        return False