from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i]!=0:
                res.append(nums[i])
        if len(res)<=1:
            return 0
        res = [abs(x) for x in res]
        res.sort()
        lim = 10**5
        a = res[-1]*res[-2]*lim

        return abs(a)