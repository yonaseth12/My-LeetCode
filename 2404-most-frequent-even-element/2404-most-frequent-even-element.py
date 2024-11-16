class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return -1
        tracker_dict = {}
        for i in nums:
            if i % 2 == 1: continue
            if i in tracker_dict: tracker_dict[i] += 1
            else: tracker_dict[i] = 1
        if not tracker_dict: return -1
        smallest_even = -1
        repetition = 0
        for key, value in tracker_dict.items():
            if value > repetition:
                smallest_even = key
                repetition = value
            elif value == repetition:
                if key < smallest_even:
                    smallest_even = key
                    repetition = value
        return smallest_even
