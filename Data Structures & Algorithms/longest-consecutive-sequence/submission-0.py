class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for n in nums_set:
            # check for begining of sequence
            if n-1 not in nums_set:
                # check length of sequence
                length = 0
                while (n+length) in nums_set:
                    length += 1

                longest = max(longest, length)
                
        return longest