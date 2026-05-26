class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower=set()
        upper=set()
        for i in word:
            if i.islower():
                lower.add(i)
            else:
                upper.add(i.lower())
        count=0
        for j in lower:
            if j in upper:
                count+=1
        return count
s=Solution()
print(s.numberOfSpecialChars(word = "aaAbcBC"))