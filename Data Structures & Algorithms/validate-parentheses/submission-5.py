class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(', '}':'{', ']':'['}
        stack = []
        n = len(s)
        
        for i in range(n):
            if s[i] in hashmap:
                if stack and stack[-1]==hashmap[s[i]]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(s[i])

        if len(stack)==0:
            return True
        return False