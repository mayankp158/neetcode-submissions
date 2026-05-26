class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_hash = {}
        l = 0
        n = len(s)
        res=0
        max_f = 0

        for r in range(n):
            count_hash[s[r]] = 1 + count_hash.get(s[r], 0)
            max_f = max(max_f, count_hash[s[r]])
            
            while (r - l + 1) - max_f > k:
                count_hash[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res