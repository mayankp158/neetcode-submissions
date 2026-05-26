class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        
        # right nearest small
        right_small = [0]*n
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack)==0:
                right_small[i] = n
            else:
                right_small[i] = stack[-1]
            stack.append(i)

        while len(stack)>0:
            stack.pop() 

        # left nearest small
        left_small = [0]*n
        for i in range(0, n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack)==0:
                left_small[i] = -1
            else:
                left_small[i] = stack[-1]
            stack.append(i)
            
        max_area = 0

        for i in range(0,n):
            width = right_small[i]-left_small[i]-1
            area = heights[i]*width
            max_area = max(area, max_area)

        return max_area



