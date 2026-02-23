"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        b = set(nums)
        res = []
        for i in range(1,len(nums)):
            if i not in b:
                res.append(i)
        if len(b) + len(res) != len(nums):
            res.append(len(nums))
        return res
"""