class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for i in nums:
            sum = sum ^ i
        return sum
        