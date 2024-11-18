class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        common_min = -1
        i1, i2 = 0, 0
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] == nums2[i2]:
                common_min = nums1[i1]
                break
            elif nums1[i1] > nums2[i2]:
                    i2 += 1
            else: i1 += 1
        
        return common_min