class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        new_str = ""

        for i in s:
            if i.isalnum():
                new_str += i.lower() 
        n = len(new_str)
        end = n-1

        while start<end:
            if new_str[start] == new_str[end]:
                start += 1
                end -= 1
            else:
                return False
        return True