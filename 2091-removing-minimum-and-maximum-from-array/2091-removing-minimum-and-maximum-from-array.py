class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_idx = 0
        max_idx = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[min_idx]: min_idx = i
            if nums[i] > nums[max_idx]: max_idx = i
        length = len(nums)
        first_idx = min(min_idx, max_idx)
        second_idx = max(min_idx, max_idx)
        opt1 = second_idx + 1  # deleting both from front
        opt2 = length - first_idx     # deleting both from back
        opt3 = (first_idx+1) + (length - second_idx)     # deleting from both back and front
        
        return min(opt1, opt2, opt3)
        
        
        