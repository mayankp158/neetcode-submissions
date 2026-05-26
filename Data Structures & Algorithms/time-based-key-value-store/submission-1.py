class TimeMap:

    # approach 

    # hashmap = {}
    # set:
    #     hashmap[key] = {timestamp:value}
    # get:
    #     if timestamp in hashmap[key].keys():
    #         returnhashmap[key][timestamp]
    #     else:
    #         return hashmap[key][list(hashmap[key].keys())[-1]]

    # approach 

    # hashmap = {}
    # set:
    #     if key not in hashmap
    #     hashmap[key] = []
    #     hashmap[key].append([value, timestamp])
    # get:
    #     if key in hashmap
    #     apply binary search
    #     l = 0 
    #     r = len(hashmap[key])-1
    #     res=""

    #     while l<=r:
    #         mid = (l+r)//2
    #         check exact match
    #         if hashmap[key][mid][1]==timestamp
    #         return hashmap[key][mid][0]
    #         check prev timestamp of given timestamp
    #         if hashmap[key][mid][1]<timestamp
    #         res = hashmap[key][mid][0]
    #         l=mid+1
    #         else
    #         r=mid-1
    #     return res
        

    def __init__(self):
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.hashmap:
            n = len(self.hashmap[key])
            l = 0
            r = n-1
            while l<=r:
                mid = (l+r)//2

                #exact match 
                if self.hashmap[key][mid][1]==timestamp:
                    res = self.hashmap[key][mid][0]
                    return res
                # check prev timestamp of given timestamp
                elif self.hashmap[key][mid][1]<timestamp: 
                        res = self.hashmap[key][mid][0]
                        l = mid+1
                else:
                    r=mid-1
        return res

            