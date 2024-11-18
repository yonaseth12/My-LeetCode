class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_dict, nums2_dict = {}, {}
        for i in nums1:
            if i in nums1_dict: nums1_dict[i] += 1
            else: nums1_dict[i] = 1
        for i in nums2:
            if i in nums2_dict: nums2_dict[i] += 1
            else: nums2_dict[i] = 1
        intersection = {}
        for key, value in nums1_dict.items():
            if key in nums2_dict: intersection[key] = min(value, nums2_dict[key])
        intersection_list = []
        for key, value in intersection.items():
            list_to_add = [key] * value
            intersection_list.extend(list_to_add)
        return intersection_list