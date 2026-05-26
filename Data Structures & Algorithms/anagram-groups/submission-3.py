class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res = []

        for s in strs:
            arr = [0]*26
            for i in s:
                arr[ord(i)-ord('a')] += 1
            
            if tuple(arr) not in hashmap:
                hashmap[tuple(arr)] = [s]
            else:
                hashmap[tuple(arr)].append(s)

        for j in hashmap:
            res.append(hashmap[j])

        return res
