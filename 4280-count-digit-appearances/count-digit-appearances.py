class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
            count=0
            for i in "".join(str(nums)):
                if i.isdigit():
                    if int(i)==digit:
                        count+=1
            return count
s=Solution()
print(s.countDigitOccurrences(nums = [12,54,32,22], digit = 2))