class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # approach

        # slow = 0
        # fast  = 0
        
        # # find intersection point
        # move slow by = nums[slow] -> [0, 1], [1, 2]
        # move fast by = nums[nums[fast]] -> [1, 2], [3, 2]
        # if slow == fast:
        #     break

        # # cycle start point
        # slow2 = 0
        # move slow2 = nums[slow2]
        # move slow = nums[slow]
        # if slow==slow2:
        #     return slow

        slow = 0
        fast = 0

        while True:
            slow = nums[slow] 
            fast = nums[nums[fast]] 

            if slow == fast:
                break

        slow2 = 0

        while True:
            slow2 = nums[slow2]
            slow = nums[slow]

            if slow == slow2:
                return slow