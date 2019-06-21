class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #combine nums1, num2
        temp = nums1 + nums2
        temp.sort()
        if len(temp) == 2:
            return (temp[0]+temp[1])/2
        elif len(temp) % 2 == 0:
            first = len(temp) // 2
            before = first - 1
            return (temp[first]+temp[before]) / 2
        else:
            return temp[len(temp) // 2] 