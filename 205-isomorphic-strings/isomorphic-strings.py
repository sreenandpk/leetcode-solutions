class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        used = []

        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            else:
                if t[i] in used:
                    return False
                mapping[s[i]] = t[i]
                used.append(t[i])

        return True

s = Solution()
print(s.isIsomorphic("egg", "add"))