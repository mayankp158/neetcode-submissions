class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonic decreasing stack problem
        # descreasing -> top is less and start is greatest
        # increasing -> top is greatest and start is less

        stack = []
        n = len(temperatures)
        res = [0]*n # index, temp

        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][1]:
                index_top, temp_top = stack[-1][0], stack[-1][1]
                res[index_top] = i - index_top
                stack.pop()
            stack.append([i, t])
        
        return res