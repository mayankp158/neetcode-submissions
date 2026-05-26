class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)

        l = 1
        r = max(piles)
        final = r

        while l<=r:
            m = (l+r)//2
            res=0
            for i in range(len(piles)):
               res += math.ceil(piles[i]/m)

            if res<=h:
                final = min(final,m)
                r = m-1
            elif res>h:
                l = m+1

        return final
