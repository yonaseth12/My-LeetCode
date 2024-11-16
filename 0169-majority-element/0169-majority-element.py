class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3: return nums[0]
        threshold_num = (len(nums) // 2) + 1
        tracker_dict = {}
        for i in nums:
            if i in tracker_dict:
                tracker_dict[i] += 1
            else: tracker_dict[i] = 1
        major_num, rep = None, 0
        for key, value in tracker_dict.items():
            if value >= threshold_num: return key