class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # approach
        # create new array 
        # arr = nums1 + nums2
        # n = len(arr)

        # if n%2!=0:
        #     m = n//2
        #     ans = float(arr[m])
        # else:
        #     m = n//2
        #     prev = m-1
        #     sum_median = arr[m]+arr[prev]
        #     ans = float(sum_median/2)

        # return ans

        arr = sorted(nums1 + nums2)
        n = len(arr)

        if n%2!=0:
            m = n//2
            ans = float(arr[m])
        else:
            m = n//2
            prev = m-1
            sum_median = arr[m]+arr[prev]
            ans = float(sum_median/2)

        return ans