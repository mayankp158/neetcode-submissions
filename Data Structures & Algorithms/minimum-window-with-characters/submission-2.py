class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # approach - 1 (not the exact optimal solution => comparison will be done for each char freq)

        # create two maps that counts freq of characters
        # map_str_t -> iterate on str t and count freq of chars
        # map_str_s -> iterate on str s until map_str_s contains freq of chars>= freq of chars of map_str_t
        # keep shrinking widow of valid string (contains all char) until smallest window is found
        # return smallest window substr

        # approach - 2
        # create hashmap for counting freq -> t = hashmap_t
        # populate hashmap using basic approach
        # create hashmap for counting freq -> s = hashmap_s
        # have = 0, need = len(hashmap_t)
        # res = [-1, -1]
        # reslen = infinity
        # for r in range(len(s)):
        #     if s[r] in hashmap_s:
        #         hashmap_s[s[r]] += 1 
        #     else:
        #         hashmap_s[s[r]] = 1

        #     if s[r] in hashmap_t and hashmap_s[s[r]] == hashmap_t[s[r]]:
        #         have += 1

        #     while have == need:
        #         update res
        #         if (r-l+1)<reslen:
        #             res = [l,r]
        #             reslen = (r-l+1)
        #         shrink window by poping value from start
        #         hashmap_s[s[l]] -= 1
        #         if s[l] in hashmap_t[s[r]] and hashmap_t[s[l]]<hashmap_s[s[l]]:
        #             have -= 1
        #         l += 1
            
        #     l, r = res

        #     return s[l:r+1] if reslen != infinity else '' 

        hashmap_t = {}

        for c in t:
            if c in hashmap_t:
                hashmap_t[c] += 1
            else:
                hashmap_t[c] = 1

        hashmap_s = {}
        n = len(s)
        have = 0
        need = len(hashmap_t)
        res = [-1,-1]
        reslen = float('inf')
        l = 0

        for r in range(n):
            if s[r] in hashmap_s:
                c = s[r]
                hashmap_s[c] += 1
            else:
                c = s[r]
                hashmap_s[c] = 1
            
            if c in hashmap_t and hashmap_t[c] == hashmap_s[c]:
                have += 1
            
            while have == need:
                # update values of min window
                if (r-l+1) < reslen:
                    res = [l,r]
                    reslen = (r-l+1)
                # shrink window
                hashmap_s[s[l]] -= 1
                if s[l] in hashmap_t and hashmap_s[s[l]] < hashmap_t[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if reslen != float('inf') else '' 
