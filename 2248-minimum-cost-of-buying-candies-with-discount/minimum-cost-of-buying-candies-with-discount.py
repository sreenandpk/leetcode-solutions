class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        total = 0
        for i in range(len(cost)):
            if (i + 1) % 3 != 0:
                total += cost[i]
        return total
s=Solution()
print(s.minimumCost(cost = [6,5,7,9,2,2]))