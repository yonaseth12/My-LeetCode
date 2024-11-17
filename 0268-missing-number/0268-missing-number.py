class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = -1
        sum = 0
        for i in nums:
            if i > max_num: max_num = i
            sum += i
        supposed_sum = 0
        for i in range(max_num+1):
            supposed_sum += i
        if supposed_sum == sum:
            if len(nums) == max_num: return 0
            else: return max_num + 1
        else: return supposed_sum - sum
        