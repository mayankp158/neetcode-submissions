class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mid_index = n//2
      
        if target < nums[mid_index]:
            for i in range(mid_index):
                if nums[i] == target:
                    return i
        
        if target > nums[mid_index]:
            for i in range(mid_index+1, n):
                if nums[i] == target:
                    return i
        
        if target == nums[mid_index]:
            return mid_index

        else:
            return -1

        