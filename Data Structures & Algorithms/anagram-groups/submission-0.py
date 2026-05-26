from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sorted_string = ''.join(sorted(s))
            res[sorted_string].append(s)

        return res.values()        