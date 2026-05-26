class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr_set = set(nums)
        n = len(nums)
        res = []

        if len(nums) == 0:
            return 0
        for i in range(n):
            long_con_arr = 1
            val = nums[i]
            if (val-1) not in arr_set:
                while val+1 in arr_set:
                    long_con_arr += 1
                    val = val+1
                res.append(long_con_arr)
            else:
                continue
        
        return max(res)