class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        idx_dict = {}
        for i in range(len(nums2)):
            idx_dict[nums2[i]] = i
        nextg_list = []
        for i in range(len(nums1)):
            isGreaterFound = False
            for j in range(idx_dict[nums1[i]], len(nums2)):
                if nums1[i] < nums2[j]:
                    nextg_list.append(nums2[j])
                    isGreaterFound = True
                    break
            if not isGreaterFound: nextg_list.append(-1)
        return nextg_list