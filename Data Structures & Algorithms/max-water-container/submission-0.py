class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        max_area = 0

        while l<r:
            w = r-l
            h = min(heights[l],heights[r])
            curr_area = w*h
            max_area = max(curr_area,max_area)

            if heights[l]<heights[r]:
                l += 1
            else:
                r -= 1

        return max_area