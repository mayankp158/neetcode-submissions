class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_1 = {}
        hashmap_2 = {}

        for i in s:
            if i in hashmap_1:
                hashmap_1[i] += 1
            else:
                hashmap_1[i] = 0
        
        for j in t:
            if j in hashmap_2:
                hashmap_2[j] += 1
            else:
                hashmap_2[j] = 0

        if hashmap_1==hashmap_2:
            return True
        return False