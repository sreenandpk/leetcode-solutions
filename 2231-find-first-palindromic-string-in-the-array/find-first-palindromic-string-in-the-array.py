from typing import List
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            rev=""
            for j in range(len(i)-1,-1,-1):
                rev+=i[j]
            if rev!=i:
                rev=""
            else:
                return rev
        return ""    
s=Solution()
print(s.firstPalindrome(words = ["def","ghi"]))