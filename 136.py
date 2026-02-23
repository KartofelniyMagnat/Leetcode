"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        b = set()
        a = list()
        for element in nums:
            if element in b:
                a.append(element)
            else:
                b.add(element)
        for element in nums:
            if element not in a:
                return element
"""
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            res ^= n
        
        return res
"""
# bit manipulation with XOR
# when we get numbers [2,3,5,3,5] the code is working like 2 ^ 3 ^ 5 ^ 3 ^ 5 = 2 ^ (3^3) ^ (5^5) = 2 ^ 0 ^ 0 = 2
