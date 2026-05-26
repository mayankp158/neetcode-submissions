class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # approach

        # n = len(s1)
        # calculate freq of elements in s1 and create a hashmap
        # create window of size = n
        # use this window from l = 0, r = n-1
        # calculate freq of elements in s2 for the window l to r in hashmap
        # compare with hashmap of s1 with the hashmap of s2 fopr given window 
        # if matches return true
        # else shift window to right side by l +=1, r +=1
        # if there is no match and r reaches len(s2)-1 then return false

        n = len(s1)

        hashmap_s1 = {}

        for i in s1:
            if i in hashmap_s1:
                hashmap_s1[i] += 1
            else:
                hashmap_s1[i] = 1

        l = 0
        r = n-1

        while r<len(s2):
            hashmap_s2 = {}
            for i in s2[l:r+1]:
                if i in hashmap_s2:
                    hashmap_s2[i] += 1
                else:
                    hashmap_s2[i] = 1

            if hashmap_s1 == hashmap_s2:
                return True
            else:
                l += 1
                r += 1
                hashmap_s2={}

        return False