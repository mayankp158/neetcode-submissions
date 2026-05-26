class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
    
        for i in tokens:
            if i == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b+a)
            elif i == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif i == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)
            elif i == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a)) # used to truncate towards zero
            else:
                stack.append(int(i))
        return stack[0]