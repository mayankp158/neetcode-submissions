class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        for i in nums:
            if i not in hashmap:
                hashmap.add(i)
            else:
                return True
        return False