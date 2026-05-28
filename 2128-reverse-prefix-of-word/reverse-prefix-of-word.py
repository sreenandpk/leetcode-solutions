class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        prefix=""
        index=word.index(ch)
        for i in range(index,-1,-1):
            prefix+=word[i]
        for j in range(index+1,len(word)):
            prefix+=word[j]
        return prefix
s=Solution()
print(s.reversePrefix(word = "abcdefd", ch = "d"))