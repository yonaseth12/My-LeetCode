class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while True:
            if len(nums) == 1:
                return nums[0]
            new_nums = []
            for i in range(len(nums)-1):
                new_nums.append((nums[i] + nums[i+1])%10)
            nums = new_nums