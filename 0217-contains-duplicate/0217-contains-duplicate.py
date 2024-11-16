class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique_set = set()
        for i in nums:
            if i in unique_set: return True
            else: unique_set.add(i)
        
        return False