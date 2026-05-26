class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # single pass
        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i
        
        # # double pass
        # hashmap = {}

        # for i, n in enumerate(nums):
        #     hashmap[n] = i

        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in hashmap and hashmap[diff] != i:
        #         return [i, hashmap[diff]]