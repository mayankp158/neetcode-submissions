class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums = sorted(nums,reverse=False)
        
        for i in range(n):
            j = i+1
            k = n-1
            if (i>0 and nums[i]==nums[i-1]):
                continue
            while j<k:
                three_sum = nums[i] + nums[j] + nums[k] 
                if three_sum<0:
                    j += 1
                elif three_sum>0:
                    k -= 1
                else:
                    if three_sum == 0:
                        res.append([nums[i],nums[j],nums[k]])
                        j += 1
                        k -= 1
                        while (j<k and nums[j]==nums[j-1]):
                            j += 1
        return res
