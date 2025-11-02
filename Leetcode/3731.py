from typing import List
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        maxx= max(nums)
        minn = min(nums)
        rangee = set(range(minn,maxx+1))
        miss = sorted(rangee - set(nums))
        return miss