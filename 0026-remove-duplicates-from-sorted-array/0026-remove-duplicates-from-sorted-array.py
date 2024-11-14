class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        tracker_list = []
        initial_length = len(nums)
        iteration_i = 0
        pointer_i = 0
        
        while iteration_i < initial_length:
            if nums[pointer_i] in tracker_list:
                nums.pop(pointer_i)
                iteration_i += 1
            else:
                tracker_list.append(nums[pointer_i])
                iteration_i += 1
                pointer_i += 1
        return pointer_i
                