class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # approach

        # calculate frequency of characters in s1 using hashmap
        # create sliding window on s2 of size len(s1)
        # maintain frequency hashmap for current window in s2
        # initially expand window by adding characters from right side
        # if window size exceeds len(s1):
        # remove left character frequency from hashmap
        # if frequency becomes 0, delete the key
        # move left pointer ahead
        # compare hashmap of s1 and current window hashmap of s2
        # if both match, permutation exists -> return True
        # continue sliding window till end of s2
        # if no matching window found, return False

        n1 = len(s1)
        n2 = len(s2)

        hashmap_s1 = {}

        for i in s1:
            if i in hashmap_s1:
                hashmap_s1[i] += 1
            else:
                hashmap_s1[i] = 1

        l = 0
        r = n1-1
        window = n1
        hashmap_s2 = {}

        for r in range(n2):
            if s2[r] in hashmap_s2:
                hashmap_s2[s2[r]] += 1
            else:
                hashmap_s2[s2[r]] = 1

            if (r-l+1)>window:
                hashmap_s2[s2[l]] -= 1
                if hashmap_s2[s2[l]] == 0:
                    del hashmap_s2[s2[l]]
                l+=1
            if hashmap_s1 == hashmap_s2:
                return True

        return False