class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # prefix = [1]*n
        # suffix = [1]*n
        # ans = [1]*n
        # for i in range(1, n):
        #     prefix[i] = prefix[i-1] * nums[i-1]
        
        # for j in range(n-2, -1, -1):
        #     suffix[j] = suffix[j+1] * nums[j+1]

        # for k in range(0, n):
        #     ans[k] = prefix[k]*suffix[k]

        # return ans


        n = len(nums)
        ans = [1]*n
        prefix = 1
        suffix = 1

        for i in range(1, n):
            prefix = prefix * nums[i-1]
            ans[i] = prefix
        
        for j in range(n-2, -1, -1):
            suffix = suffix * nums[j+1]
            ans[j] = suffix * ans[j]

        return ans