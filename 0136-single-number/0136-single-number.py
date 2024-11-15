class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tracker_dict = {}
        for i in nums:
            if i in tracker_dict:
                del tracker_dict[i]
            else: tracker_dict[i] = 1
        key, value = next(iter(tracker_dict.items()))
        return key
        