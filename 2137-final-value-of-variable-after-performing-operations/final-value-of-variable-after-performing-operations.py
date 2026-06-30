from typing import List
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count=0
        for i in operations:
            if "+" in i:
                count+=1
            else:
                count-=1
        return count
s=Solution()
print(s.finalValueAfterOperations(operations = ["++X","++X","X++"]))