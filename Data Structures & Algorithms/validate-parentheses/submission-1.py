class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_para_dict = {')':'(', '}':'{', ']':'['}

        for i in s:
            if i in closing_para_dict:
                if stack and stack[-1] == closing_para_dict[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        if len(stack) == 0:
            return True
        return False
