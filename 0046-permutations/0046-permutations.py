class Solution(object):
        
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutation = []
        if len(nums) == 0: return [[]]
        if len(nums) == 1: return [nums]
        for i in nums:
            complement_list = nums[:]
            complement_list.remove(i)
            for innerList in self.permute(complement_list):
                permutation.append([i]+innerList)
        return permutation
            
        