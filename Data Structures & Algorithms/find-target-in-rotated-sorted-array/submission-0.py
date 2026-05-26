class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st = 0
        end = len(nums)-1
        
        #LSR
        while st<=end:
            mid = (st+end)//2
            if nums[mid]==target:
                return mid
            if nums[st]<=nums[mid]:
                if target>=nums[st] and target<=nums[mid]:
                    end = mid-1
                else:
                    st = mid+1
            #RSR
            else:
                if nums[st]>=nums[mid]:      
                    if target>=nums[mid] and target<=nums[end]:
                        st = mid+1
                    else:
                        end = mid-1
        return -1









