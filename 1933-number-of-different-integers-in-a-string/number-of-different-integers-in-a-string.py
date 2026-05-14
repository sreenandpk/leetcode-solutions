class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s=""
        values=set()
        for i in word:
            if i.isdigit():
                s+=i
            else:
                s+=" "
        nums=s.split()
        for j in nums:
            values.add(int(j))
                    
        return len(values)
s=Solution()
print(s.numDifferentIntegers(word = "a123bc34d8ef34"))