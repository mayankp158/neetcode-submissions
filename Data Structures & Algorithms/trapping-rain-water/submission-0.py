class Solution:
    def trap(self, height: List[int]) -> int:
        # formula
        # ans += min(lmax, rmax) - h[i]

        # lmax = [0, 2, 2, 3, 3, 3, 3, 3, 3, 3]
        # rmax = [3, 3, 3, 3, 3, 3, 3, 3, 2, 1]

        # ans = 0-0 = 0
        # ans = 2-2= 0
        # ans = 2-0= 2
        # ans = 3-3= 0
        # ans = 3-1= 2
        # ans = 3-0= 3
        # ans = 3-1= 2
        # ans = 3-3= 0
        # ans = 2-2= 0
        # ans = 1-1= 0

        # final = 2+2+3+2=9

        n = len(height)
        lmax = [height[0]]*n
        rmax = [height[n-1]]*n
        ans = 0

        for i in range(1,n):
            lmax[i] = max(lmax[i-1], height[i])

        for j in range(n-2,-1, -1):
            rmax[j] = max(rmax[j+1], height[j])

        for k in range(n):
            ans += min(lmax[k], rmax[k]) - height[k]

        return ans

        