class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        initial_length = len(nums)
        iterator_i = 0
        pointer_i = 0
        
        while iterator_i < initial_length:
            if nums[pointer_i] == val:
                nums.pop(pointer_i)
                iterator_i += 1
            else:
                pointer_i += 1
                iterator_i += 1
        return pointer_i