class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res = []
        for i in strs:
            sorted_str = tuple(sorted(i))
            if sorted_str not in hashmap:
                hashmap[sorted_str] = [i]
            else:
                hashmap[sorted_str].append(i)

        for j in hashmap:
            res.append(hashmap[j])

        return res