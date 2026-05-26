import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            tmp = nums[i]
            nums[i] = 1
            product = math.prod(nums)
            nums[i] = tmp
            res.append(product)
        return res