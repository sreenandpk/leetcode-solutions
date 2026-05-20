from typing import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d={}
        for i in range(len(list1)):
            d[list1[i]]=i
        minimum=float("inf")
        result=[]
        for j in range(len(list2)):
            if list2[j] in d:
                total=d[list2[j]]+j
                if total<minimum:
                    minimum=total
                    result=[list2[j]]
                elif total==minimum:
                    result.append(list2[j])
        return result
s=Solution()
print(s.findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]))