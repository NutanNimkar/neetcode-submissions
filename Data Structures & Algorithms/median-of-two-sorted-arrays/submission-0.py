class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedArr = self.mergeTwoArrays(nums1, nums2)
        median = 0
        n = len(mergedArr)
        if len(mergedArr) % 2 == 0:
            a = mergedArr[n // 2 - 1]
            b = mergedArr[n // 2]
            median = (a + b) / 2
        else:
            median = mergedArr[n // 2]
        return median

    def mergeTwoArrays(self, arr1, arr2):
        if not arr1:
            return arr2
        if not arr2:
            return arr1
        mergedArr = []
        i,j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                mergedArr.append(arr1[i])
                i += 1
            else:
                mergedArr.append(arr2[j])
                j += 1
        while arr1 and i < len(arr1):
            mergedArr.append(arr1[i])
            i += 1
        while arr2 and j < len(arr2):
            mergedArr.append(arr2[j])
            j += 1
        return mergedArr


