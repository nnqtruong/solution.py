class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        tempnum = []
        for i in range(m):
            tempnum.append(nums1[i])
        for i in range(n):
            tempnum.append(nums2[i])
        tempnum.sort()
        for i in range(len(tempnum)):
            nums1[i] = tempnum[i]
        return nums1


        
