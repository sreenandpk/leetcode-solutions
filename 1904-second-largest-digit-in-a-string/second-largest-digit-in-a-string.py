class Solution:
    def secondHighest(self, s: str) -> int:
        largest=-1
        numbers=[]
        second_largest=-1
        for i in s:
            if i.isdigit():
                numbers.append(int(i))
                if int(i)>largest:
                    largest=int(i)
        for i in numbers:
            if i<largest and i>second_largest:
                second_largest=i
        return second_largest
s=Solution()
print(s.secondHighest("dfa12321afd"))